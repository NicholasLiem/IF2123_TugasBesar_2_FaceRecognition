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

def euclideanDistance(cobaNyimpen1, cobaNyimpen2):
    total = 0
    for i in range (len(cobaNyimpen1)):
        total += (cobaNyimpen1[i] - cobaNyimpen2[i])**2
    return np.sqrt(total)

def main():
    database = []
    matrixbaru = []
    
    ip.read_training_data_set("Zoe Saldana", database)
    meandatabase = mean_database(database, mp.mean_phi(database))
    for item in meandatabase:
        matrixbaru.append(item.reshape(w*h, 1))
    
    matKov = matCov(matrixbaru)
    matrixA = concate(matrixbaru)
    eigenval, eigenvec = np.linalg.eig(matKov)
    eigenFaceArray = []
    
    K = 10
    for i in range(K):
        eigenFaceArray.append(np.matmul(matrixA, eigenvec[i]))

    # eigenface_titles = ["eigenface %d" % i for i in range(len(eigenFaceArray))]
    # plot_portraits(eigenFaceArray, eigenface_titles, h, w, 5, 2)
    # plt.show()

    #"Database koefisien2 semua wajah"
    nilaiX = []
    for i in range(len(database)):
        cobaNyimpen = []
        for j in range(K):
            cobaNyimpen.append(np.dot(meandatabase[i].reshape(w*h, 1).T, eigenFaceArray[j]))
        nilaiX.append(cobaNyimpen)

    testImage = ip.read_image("testing.jpg")
    testImage = abs(testImage-mp.mean_phi(database))
    nilai2 = []
    for i in range(len(database)):
        cobaNyimpen = []
        for j in range(K):
            cobaNyimpen.append(np.dot(testImage.reshape(w*h, 1).T, eigenFaceArray[j]))
        nilai2.append(cobaNyimpen)
    
    min = euclideanDistance(nilaiX[0], nilai2[0])
    index = 0
    for i in range(len(nilaiX)):
        dist = euclideanDistance(nilaiX[i], nilai2[0])
        print(dist)
        if dist < min:
            min = dist
            index = i
    print(min)
    print(index)
    ip.print_img(database[index])
    # print(len(eigenFaceArray))
    # eigenface_titles = ["eigenface %d" % i for i in range(len(eigenFaceArray))]
    # plot_portraits(eigenFaceArray, eigenface_titles, h, w, 5, 4)
    # plt.show()
    

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
        res.append(abs(m-mean)*1/10000000)
    return res

main()