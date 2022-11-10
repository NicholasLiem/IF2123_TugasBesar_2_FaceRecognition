import cv2
import numpy as np
import os
import timeHandling as t
from PIL import Image as im

w, h = 256,256

imgfaces = []
def read_training_data_set(nama):
    path = os.getcwd()
    path = path + "\\test\\training\\" + nama
    dir_list = os.listdir(path)
    for pic in dir_list:
        if pic.endswith('.jpg'):
            img = cv2.imread(path + '\\' + pic, cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (w, h))
            imgfaces.append(img)
    print("Dataset has been loaded.")

def mean_phi(dataset):
    mean = np.zeros((w, h))
    for img in dataset:
        mean += img
    mean = mean / len(dataset)
    return mean

# def find_covariance(dataset):
#     mean = mean_phi(dataset)
#     cov = dataset[1] - mean
#     for i in range (1, len(dataset)):
#         avg = dataset[i] - mean
#         dataset[i] = avg
#         cov = np.concatenate((cov, avg), axis=1)
#     cov_mat = np.cov(dataset, rowvar = False)
#     return cov_mat

def find_covariance(dataset):
    mean = mean_phi(dataset)
    cov = dataset[0] - mean
    for i in range (1, len(dataset)):
        cov = np.concatenate((cov, dataset[i] - mean), axis=1)
    return np.matmul(cov, cov.T)

def norm(vector):
    norm = 0
    for i in vector:
        norm += (i ** 2)
    norm = norm ** (1/2)
    return norm

def ortho(u,temp):
    ortho = 0
    norm2 = norm(u) ** 2
    for i in range(len(u)):
        ortho += (u[i] * temp[i])
    ortho /= norm2
    ortho = np.multiply(ortho, u)
    return ortho

def getQR(matrix):
    n = len(matrix)
    q = [[0 for i in range(n)] for j in range(n)]
    q = np.reshape(q, (n, n))
    q = q.astype('float')
    r = [[0 for i in range(n)] for j in range(n)]
    r = np.reshape(r, (n, n))
    temp = [0 for i in range(n)]
    for i in range(n):
        temp = np.array(matrix[:, i])
        temp = np.reshape(temp, n)
        for j in range(0, i):
            u = np.array(q[:, j])
            u = np.reshape(u, n)
            temp = np.subtract(temp, ortho(u, temp))
        for k in range(n):
            q[k][i] = temp[k]
    for l in range(n):
        temp = np.array(q[:, l])
        temp = np.reshape(temp, n)
        temp = np.divide(temp, norm(temp))
        for m in range(n):
            q[m][l] = temp[m]
    r = np.dot(q.T, matrix)
    return q, r

def isTriangle(matrix):
    triangle = True
    for i in range(1, len(matrix)):
        for j in range(i):
            if (matrix[i][j] > 0.0001 or matrix[j][i] < -0.0001):
                triangle = False
    return triangle

def find_eigen(cov):
    a = cov
    triangle = False
    n = len(cov)
    eVec = np.eye(n)
    count = 0
    while (not(triangle)):
        q,r = getQR(a)
        triangle = isTriangle(np.dot(r, q))
        if (not(triangle)):
            a = np.dot(r, q)
            eVec = np.dot(eVec, q)
    e = [a[i][i] for i in range(n)]
    return e, eVec

def sort_eigen(cov):
    eigenVal, eigenVec  = np.linalg.eig(cov)
    idx = eigenVal.argsort()[::-1]
    eigenVal = eigenVal[idx]
    eigenVec = eigenVec[:,idx]
    return eigenVec

def __main__():
    read_training_data_set("Robert Downey Jr")
    t.tic()
    #eigenval, eigenvec = np.linalg.eig(find_covariance(imgfaces))
    #print(eigenval)
    #print(eigenvec)
    e, q = find_eigen(find_covariance(imgfaces))
    #print(e)
    #print(q)   
    eigens = sort_eigen(find_covariance(imgfaces))
    print((eigens.T)[0].shape)
    res = np.matmul(eigens, imgfaces[0]-mean_phi(imgfaces))
    data = im.fromarray(res)
    data.show()
    
    # path = os.getcwd()
    # path = path + "\\test\\training\\" + "testing.jpg"
    # newImg = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    # newImg = cv2.resize(newImg, (w, h))
    
    # uNew = np.matmul(eigen, (newImg - mean_phi(imgfaces)))
    # nilaiI = 0
    # for i in range(len(imgfaces)):
    #     dist = np.linalg.norm(uNew - eigen_face(find_covariance(imgfaces), imgfaces, i))
    #     if i == 0:
    #         temp = dist
    #     elif (dist < temp):
    #         temp = dist
    #         nilaiI = i
    # print("Euclidean distance :", temp)
    # data = im.fromarray(eigen_face(find_covariance_method_concatenate(imgfaces), imgfaces))
    t.tac()
    # data.show()

if __name__ == '__main__':
    __main__()