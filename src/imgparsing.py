import cv2
import os
import matplotlib.pyplot as plt

w, h = 256, 256

# Fungsi yang menyimpan image sebagai array dan menampungkan pada sebuah database #
def read_training_data_set(nama, dataset, datalabel):
    path = os.getcwd()
    path = path + "\\test\\database\\" + nama
    dir_list = os.listdir(path)
    for pic in dir_list:
        if pic.endswith('.jpg'):
            img = cv2.imread(path + '\\' + pic, cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (w, h))
            dataset.append(img)
            datalabel.append(pic)
    print("Dataset has been loaded.")

# Fungsi yang membaca image ke array dgn membaca file #
def read_image(nama):
    path = os.getcwd()
    path = path + "\\test\\testimage\\" + nama
    newImg = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    newImg = cv2.resize(newImg, (w, h))
    return newImg

# Fungsi yang digunakan untuk melakukan penampilan wajah #
def print_img(img):
    plt.imshow(img, cmap='gray')
    plt.show()