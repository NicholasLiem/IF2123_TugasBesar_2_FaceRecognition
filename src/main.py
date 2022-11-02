import cv2
import numpy as np
import random
import os

w, h = 250, 250

def grayscale_img():
    path = os.getcwd()
    path = path + "\\test\\testImg"
    dir_list = os.listdir(path)
    for pic in dir_list:
        if pic.endswith('.jpg'):
            img = cv2.imread(path + '\\' + pic)
            resized_img = cv2.resize(img, (w, h))
            os.chdir(path)
            fileName = 'lmao.jpg'
            gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(fileName, gray)
    
    # for items in arr:
    #     print(items)
    # # cv2.waitKey(0)
    # # cv2.destroyAllWindows()
    # # cv2.waitKey(1)

def __main__():
    grayscale_img()

if __name__ == '__main__':
    __main__()