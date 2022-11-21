# Bagian Import File-File Pembantu #
import numpy as np
import timehandling as t
import imgparsing as ip
import matrixprocessing as mp
import eigenvector as ev

def process(database, testImage):

    # n adalah jumlah gambar pada database
    n = len(database)
    # n1 adalah jumlah 1/2 dari jumlah gambar pada database
    n1 = round(n/2)
    # membatasi nilai n1 agar tidak lebih dari 35
    # nilai n1 digunakan untuk membatasi jumlah eigenface yang akan digunakan
    if (n1 > 35):
        n1 = 35

    # mencari muka mean dari database
    mean = mp.mean_phi(database)

    # melakukan pengurangan gambar pada database terhadap gambar rata-rata
    training = mp.training(database,mean)

    # membentuk matriks A (concat semua gambar ditraining jadi satu matriks)
    A = mp.matrix_A(training)

    # mencari matriks kovarian A^T * A
    covMat = mp.find_covariance(A)

    # mencari nilai eigen vector dari matriks kovarian
    eigenVal, eigenVec = ev.find_eigen(covMat)

    # EFD adalah singkatan dari EigenFaceDatabase
    e, eigenFaceVector = mp.EFD1(database, A, training, eigenVec)

    # proses pembacaan gambar uji
    sampleImg = ip.read_image(testImage)

    # melakukan "normalisasi" gambar uji dengan menguranginya dengan rata-rata gambar database
    selisihSam = (sampleImg-mean).reshape((256*256,1))

    # mencari koefisien atau berat dari matriks gambar uji
    w = np.zeros((1,n1))
    for j in range (n1):
        w[0][j] = np.dot(e[j].T,selisihSam)

    # mencari jarak euclidean gambar uji terhadap setiap gambar database 
    euclideanDistanceList = mp.EDL(eigenFaceVector, w)

    # index gambar dengna jarak euclidean terkecil
    idx = mp.findClosestImageIdx(euclideanDistanceList)

    # mencari % match gambar uji dengan gambar dengan euclidean distance terkecil
    mp.percent_match(w, euclideanDistanceList[idx], n1)
    print("Closest image index: " + str(idx))
    return idx

def __main__():
    t.tic()
    database = []
    datalabel = []
    ip.read_training_data_set("Gabungan", database,datalabel)
    idx = process(database, "testing.jpg")
    ip.print_img(database[idx])
    t.tac()

if __name__ == '__main__':
    __main__()