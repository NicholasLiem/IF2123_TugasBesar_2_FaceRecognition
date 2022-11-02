import cv2
import numpy as np
import random
import os
from PIL import Image as im

w, h = 250, 250

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

def mean_phi(dataset):
    mean = np.zeros((w, h))
    for img in dataset:
        mean += img
    mean = mean / len(dataset)
    return mean

def find_covariance(dataset):
    mean = mean_phi(dataset)
    cov = dataset[0] - mean
    print(cov)
    for i in range (1, len(dataset)):
        np.concatenate((cov, dataset[i]-mean), axis=0)
    return cov

def __main__():
    read_training_data_set("Chris Hemsworth")
    cov = find_covariance(imgfaces)
    data = im.fromarray(cov)
    data.show()

if __name__ == '__main__':
    __main__()