# Bagian Import File-File Pembantu #
import numpy as np
import timehandling as t
import imgparsing as ip
import matrixprocessing as mp
import eigenvector as ev

def percent_match(w, nilai, k):
    hasil = nilai
    for i in range(k):
        hasil = hasil + w[0][i]**2
    hasil = np.sqrt(hasil)
    hasil = nilai/hasil
    hasil = 1/(1+hasil)
    print("Percent Match:", hasil*100)
    return (hasil*100)

def process(database, testImage):
    n = len(database)
    n1 = round(n/2)
    if (n1 > 35):
        n1 = 35
    mean = mp.mean_phi(database)
    covMat = mp.find_covariance(database)
    eigenVal, eigenVec = ev.find_eigen(covMat)

    e, eigenFaceVector = mp.EFD1(database, mean, eigenVec)
    sampleImg = ip.read_image(testImage)
    selisihSam = (sampleImg-mean).reshape((256*256,1))
    w = np.zeros((1,n1))
    for j in range (n1):
        w[0][j] = np.dot(e[j].T,selisihSam)
    euclideanDistanceList = mp.EDL(eigenFaceVector, w)
    idx = mp.findClosestImageIdx(euclideanDistanceList)
    percent_match(w, euclideanDistanceList[idx], n1)
    print("Closest image index: " + str(idx))
    return idx

def __main__():
    t.tic()
    database = []
    datalabel = []
    ip.read_training_data_set("Gabungan", database,datalabel)
    idx = process(database, "test123.jpeg")
    idxs = idx[0]
    ip.print_img(database[idxs])
    t.tac()

if __name__ == '__main__':
    __main__()