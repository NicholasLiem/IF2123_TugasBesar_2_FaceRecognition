import numpy as np
import matrixprocessing as mp
import imgparsing as ip
import matplotlib.pyplot as plt

w,h = 256, 256

def plot_portraits(images, titles, h, w, n_row, n_col):
    plt.figure(figsize=(2.2 * n_col, 2.2 * n_row))
    plt.subplots_adjust(bottom=0, left=.01, right=.99, top=.90, hspace=.20)
    for i in range(n_row * n_col):
        plt.subplot(n_row, n_col, i + 1)
        plt.imshow(images[i].reshape((h, w)), cmap=plt.cm.gray)
        plt.title(titles[i])
        plt.xticks(())
        plt.yticks(())

def main():
    database = []
    matrixbaru = []
    
    ip.read_training_data_set("Zendaya", database)
    meandatabase = mean_database(database, mp.mean_phi(database))
    for item in meandatabase:
        matrixbaru.append(item.reshape(w*h, 1))
    
    matKov = matCov(matrixbaru)
    matrixA = concate(matrixbaru)
    eigenval, eigenvec = np.linalg.eig(matKov)
    eigenFaceArray = []
    for i in range(len(matrixbaru)):
        eigenFaceArray.append(np.matmul(matrixA, eigenvec[i]))

    print(len(eigenFaceArray))
    eigenface_titles = ["eigenface %d" % i for i in range(len(eigenFaceArray))]
    plot_portraits(eigenFaceArray, eigenface_titles, h, w, 5, 4)
    plt.show()

    # eigenVal, eigenVec  = np.linalg.eig(matKov)
    # idx = eigenVal.argsort()[::-1]
    # eigenVal = eigenVal[idx]
    # eigenvec = eigenVec[:,idx]
    
    # eigenFace = np.matmul(matKov, )
    # ip.print_img(eigenFace)
    # eigFace1 = eigenFace[0:255, 0:255]
    

def concate(database):
    res = database[0]
    for i in range (1, len(database)):
        res = np.concatenate((res, database[i]), axis=1)
    return res
    
def matCov(meandatabase):
    cov = meandatabase[0]
    for i in range (1, len(meandatabase)):
        cov = np.concatenate((cov, meandatabase[i]), axis=1)
    return np.matmul(cov.T, cov)

def mean_database(database, mean):
    res = []
    for m in database:
        res.append(abs(m-mean))
    return res

main()