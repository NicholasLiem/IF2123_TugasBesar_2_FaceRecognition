import cv2
import numpy as np

w, h = 256, 256

def illegal_eigen_vec(matrix):
    eigenval, eigenvec = np.linalg.eig(find_covariance(matrix))
    return eigenvec

# Fungsi mencari nilai mean #
def mean_phi(dataset):
    mean = np.zeros((w, h))
    for img in dataset:
        mean += img
    mean = mean / len(dataset)
    return mean

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