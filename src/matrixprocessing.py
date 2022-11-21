import numpy as np
import eigenvector as ev

w, h = 256, 256

# Fungsi mencari nilai mean #
def mean_phi(dataset):
    mean = np.zeros((w, h))
    for img in dataset:
        mean += img
    mean = mean / len(dataset)
    return mean

# Fungsi yang digunakan untuk matriks kovarian #
def matrix_A(dataset):
    mean = mean_phi(dataset).reshape(w*h, 1)
    A = dataset[0].reshape(w*h, 1) - mean
    for i in range (1, len(dataset)):
        A = np.concatenate((A, dataset[i].reshape(w*h, 1) - mean), axis=1)
    return A

def find_covariance(dataset):
    cov = matrix_A(dataset)
    return np.matmul(cov.T, cov)

# Fungsi yang digunakan untuk mencari euclidean distance #
def EuclideanDistance(newImg, testImg):
    newImg = np.subtract(newImg, testImg)
    count = 0
    for i in range(len(newImg)):
        for j in range(len(newImg[0])):
            count += newImg[i][j]**2
    dist = np.sqrt(count)
    return dist

def EFD1(database, mean, eigenVec):
    n = len(database)
    n1 = round(n / 2)
    if (n1 > 35):
        n1 = 35
    w = np.zeros((n,n1))
    training = np.zeros((256,256))
    e = np.zeros((n1,256*256))
    for i in range(n1):
        e[i] = ev.find_eigenface(matrix_A(database),eigenVec[i])
    for i in range(n):
        training = database[i] - mean
        training = training.reshape((256*256,1))
        for j in range (n1):
            w[i][j] = np.dot((e[j].reshape((1,256*256))),training)
    return e, w

def EDL(eigenFaceDatabase, eigenFaceTest):
    eDList = []
    for i in range(len(eigenFaceDatabase)):
        eDList.append(EuclideanDistance(eigenFaceTest, eigenFaceDatabase[i]))
        # print("Distance from image " + str(i) + " is " + str(eDList[i]))
    return eDList

def findClosestImageIdx(eDList):
    min = eDList[0]
    idx = 0
    for i in range(len(eDList)):
        if eDList[i] < min:
            min = eDList[i]
            idx = i
    print("Euclidean Distance: " + str(min))
    return idx