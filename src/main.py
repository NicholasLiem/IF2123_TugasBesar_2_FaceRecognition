import cv2
import numpy as np
import random
import os

w, h = 250, 250

data_set_path = []

# def grayscale_img():
#     path = os.getcwd()
#     path = path + "\\test\\testImg"
#     dir_list = os.listdir(path)
#     for pic in dir_list:
#         if pic.endswith('.jpg'):
#             img = cv2.imread(path + '\\' + pic)
#             resized_img = cv2.resize(img, (w, h))
#             os.chdir(path)
#             fileName = 'lmao.jpg'
#             gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
#             cv2.imwrite(fileName, gray)

def read_training_data_set(nama):
    path = os.getcwd()
    path = path + "\\test\\training\\" + nama
    dir_list = os.listdir(path)
    for pic in dir_list:
        if pic.endswith('.jpg'):
            data_set_path.append(path + '\\' + pic)

def print_data_set_path():
    print(data_set_path)

def __main__():
    read_training_data_set("Chris Hemsworth")
    print_data_set_path()

if __name__ == '__main__':
    __main__()