import cv2
import numpy as np
import os
import timeHandling as t
from PIL import Image as im
import sympy as sp
from sympy import linsolve

w, h = 256, 256

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

def find_eigen(cov):
    a = cov
    for i in range(256):
        q, r = np.linalg.qr(a)
        a = np.dot(r, q)
        if i == 0:
            qvec = q
        else:
            qvec = np.dot(qvec,q)
    e = [a[i][i] for i in range(256)]
    e.sort()
    return e, qvec

def sort_eigen(cov):
    eigenVal, eigenVec  = np.linalg.eig(cov)
    idx = eigenVal.argsort()[::-1]
    eigenVal = eigenVal[idx]
    eigenVec = eigenVec[:,idx]
    return eigenVec

def __main__():
    read_training_data_set("Robert Downey Jr")
    t.tic()
    eigenval, eigenvec = np.linalg.eig(find_covariance(imgfaces))
    eigenval.sort()
    # print(eigenval)
    # print(eigenvec)
    e, q = find_eigen(find_covariance(imgfaces))
    # print(e)
    # print(q)   
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