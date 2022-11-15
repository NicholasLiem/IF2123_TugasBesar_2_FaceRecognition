import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
from PIL import Image as im

w, h = 256, 256

def read_training_data_set(nama, dataset):
    path = os.getcwd()
    path = path + "\\test\\training\\" + nama
    dir_list = os.listdir(path)
    for pic in dir_list:
        if pic.endswith('.jpg'):
            img = cv2.imread(path + '\\' + pic, cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (w, h))
            dataset.append(img)
    print("Dataset has been loaded.")

# Fungsi yang membaca image ke array dgn membaca file #
def read_image(nama):
    path = os.getcwd()
    path = path + "\\test\\test_image\\" + nama
    newImg = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    newImg = cv2.resize(newImg, (w, h))
    return newImg

def print_img(img):
    plt.imshow(img, cmap='gray')
    plt.show()
