import cv2
import numpy as np
import os
import timehandling as t
import matplotlib.pyplot as plt

w, h = 256, 256

def illegal_eigen_vec(matrix):
    eigenval, eigenvec = np.linalg.eig(matrix)
    return eigenvec

def read_training_data_set(nama, dataset):
    path = os.getcwd()
    path = path + "\\test\\database\\" + nama
    dir_list = os.listdir(path)
    for pic in dir_list:
        if pic.endswith('.jpg'):
            img = cv2.imread(path + '\\' + pic, cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (w, h))
            dataset.append(img)
    print("Dataset has been loaded.")

# Fungsi mencari nilai mean #
def mean_phi(dataset):
    mean = np.zeros((w, h))
    for img in dataset:
        mean += img
    mean = mean / len(dataset)
    return mean

# Fungsi buat menampilkan gambar #
def print_img(img):
    plt.imshow(img, cmap='gray')
    plt.show()

# Fungsi mencari matriks kovarian #
def find_covariance(dataset):
    mean = mean_phi(dataset)
    cov = dataset[0] - mean
    for i in range (1, len(dataset)):
        cov = np.concatenate((cov, dataset[i]-mean), axis=1)
    return np.matmul(cov, cov.T)

def EuclideanDistance(newImg, testImg):
    newImg = np.subtract(newImg, testImg)
    count = 0
    for i in range(len(newImg)):
        for j in range(len(newImg[0])):
            count += newImg[i][j]**2
    dist = np.sqrt(count)
    return dist

def main():
    database = []
    read_training_data_set("Robert Downey Jr", database)
    mean = mean_phi(database)
    covMat = find_covariance(database)
    eigenVec = illegal_eigen_vec(covMat)

    eigenFaceVector = []
    for i in range(len(database)):
        eigenFaceVector.append(np.matmul(eigenVec, database[i]-mean))

    sampleImg = cv2.imread("test\\testimage\\testing.jpg", cv2.IMREAD_GRAYSCALE)
    sampleImg = cv2.resize(sampleImg, (w, h))
    selisihSam = sampleImg-mean
    EigFaceSam = np.matmul(eigenVec, selisihSam)
    
    eucDistance = []
    for i in range(len(eigenFaceVector)):
        eucDistance.append(EuclideanDistance(EigFaceSam, eigenFaceVector[i]))
        print("Distance from image " + str(i) + " is " + str(eucDistance[i]))

    min = eucDistance[0]
    idx = 0
    for i in range(len(eucDistance)):
        if eucDistance[i] < min:
            min = eucDistance[i]
            idx = i
    print("The closest image is: " + str(idx))
    print_img(database[idx])

main()