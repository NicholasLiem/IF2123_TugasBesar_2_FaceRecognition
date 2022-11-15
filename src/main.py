# Bagian Import File-File Pembantu #
import numpy as np
import timehandling as t
import imgparsing as ip
import matrixprocessing as mp


def illegal_eigen_vec(matrix):
    eigenval, eigenvec = np.linalg.eig(matrix)
    return eigenvec

def process(database, testImage):
    mean = mp.mean_phi(database)
    covMat = mp.find_covariance(database)
    eigenVec = illegal_eigen_vec(covMat)

    eigenFaceVector = mp.EFD(database, mean, eigenVec)

    sampleImg = ip.read_image(testImage)
    selisihSam = sampleImg-mean
    EigFaceSam = np.matmul(eigenVec, selisihSam)
    
    euclideanDistanceList = mp.EDL(eigenFaceVector, EigFaceSam)
    for item in euclideanDistanceList:
        print(item)
    idx = mp.findClosestImageIdx(euclideanDistanceList)
    print("Closest image index: " + str(idx))
    return idx

def __main__():
    t.tic()
    database = []
    ip.read_training_data_set("Zoe Saldana", database)
    idx = process(database, "testing.jpg")
    ip.print_img(database[idx])
    t.tac()

if __name__ == '__main__':
    __main__()