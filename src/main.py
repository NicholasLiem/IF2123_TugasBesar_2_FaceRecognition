# Bagian Import File-File Pembantu #
import numpy as np
import timehandling as t
import imgparsing as ip
import matrixprocessing as mp
import eigenvector as ev

# fungi untuk menghitung % match gambar uji dengan gambar terdekatnya
def percent_match(w, nilai, k):
    hasil = nilai
    for i in range(k):
        hasil = hasil + w[0][i]**2
    hasil = np.sqrt(hasil)
    hasil = nilai/hasil
    hasil = 1/(1+hasil)
    print("Percent Match:", hasil*100)
    return (hasil*100)

# main process/program
def process(database, testImage):

    # n adalah jumlah gambar pada database
    n = len(database)

    # n1 adalah batas jumlah batasan eigen face yang akan digunakan
    n1 = round(n/2)
    if (n1 > 35):
        n1 = 35

    # mean adalah muka rata-rata dari database
    mean = mp.mean_phi(database)

    # training adalah proses mengurangi setiap gambar di database dengan rata-rata muka
    training = mp.training(database,mean)

    # A adalah matriks yang berisi konkatenasi setiap gambar di training
    A = mp.matrix_A(training)

    # covMat adalah matriks perkalian A^T * T
    covMat = mp.find_covariance(A)

    # eigenVec adalah matriks eigen vector dari covMat
    eigenVal, eigenVec = ev.find_eigen(covMat)

    # eigenFaceDatabase adalah matriks eigen face dari database
    e, eigenFaceVector = mp.EFD1(database, A, training, eigenVec)

    # pembacaan gambar uji
    sampleImg = ip.read_image(testImage)
    # 'normalisasi' gambar uji dengan mengurangi gambar uji dengan muka rata-rata
    selisihSam = (sampleImg-mean).reshape((256*256,1))

    # mengisi nilai weight gambar uji dan menyimpannya di w
    w = np.zeros((1,n1))
    for j in range (n1):
        w[0][j] = np.dot(e[j].T,selisihSam)

    # membentuk list data-data nilai euclidean distance antara gambar uji dengan gambar di database
    euclideanDistanceList = mp.EDL(eigenFaceVector, w)

    # mengeluarkan idx di mana nilai euclidean distance terkecil
    idx = mp.findClosestImageIdx(euclideanDistanceList)

    # melakukan perhitungan % match
    percent_match(w, euclideanDistanceList[idx], n1)
    print("Closest image index: " + str(idx))
    return idx, w, euclideanDistanceList, n1

def __main__():
    t.tic()
    # database = []
    # datalabel = []
    # ip.read_training_data_set("Gabungan", database, datalabel)
    # idx = process(database, "testing.jpg")
    # ip.print_img(database[idx])
    t.tac()

if __name__ == '__main__':
    __main__()