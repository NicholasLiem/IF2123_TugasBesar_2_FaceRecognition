import numpy as np

# Fungsi mencari nilai eigen dengan algoritma QR #
def eigen_qr(cov):
    a = cov
    for i in range(256):
        q, r = np.linalg.qr(a)
        a = np.dot(r, q)
    e = [a[i][i] for i in range(256)]
    return e

def norm(vector):
    norm = 0
    for i in vector:
        norm += (i ** 2)
    norm = norm ** (1/2)
    return norm

def ortho(u,temp):
    ortho = 0
    norm2 = norm(u) ** 2
    for i in range(len(u)):
        ortho += (u[i] * temp[i])
    ortho /= norm2
    ortho = np.multiply(ortho, u)
    return ortho

def getQR(matrix):
    n = len(matrix)
    q = [[0 for i in range(n)] for j in range(n)]
    q = np.reshape(q, (n, n))
    q = q.astype('float')
    r = [[0 for i in range(n)] for j in range(n)]
    r = np.reshape(r, (n, n))
    temp = [0 for i in range(n)]
    for i in range(n):
        temp = np.array(matrix[:, i])
        temp = np.reshape(temp, n)
        for j in range(0, i):
            u = np.array(q[:, j])
            u = np.reshape(u, n)
            temp = np.subtract(temp, ortho(u, temp))
        for k in range(n):
            q[k][i] = temp[k]
    for l in range(n):
        temp = np.array(q[:, l])
        temp = np.reshape(temp, n)
        temp = np.divide(temp, norm(temp))
        for m in range(n):
            q[m][l] = temp[m]
    r = np.dot(q.T, matrix)
    return q, r

def isTriangle(matrix):
    triangle = True
    for i in range(1, len(matrix)):
        for j in range(i):
            if (matrix[i][j] > 0.0001 or matrix[j][i] < -0.0001):
                triangle = False
    return triangle

def find_eigen(cov):
    a = cov
    triangle = False
    n = len(cov)
    eVec = np.eye(n)
    count = 0
    while (not(triangle)):
        q,r = getQR(a)
        triangle = isTriangle(np.dot(r, q))
        if (not(triangle)):
            a = np.dot(r, q)
            eVec = np.dot(eVec, q)
    e = [a[i][i] for i in range(n)]
    return e, eVec

def sort_eigen(cov):
    eigenVal, eigenVec  = np.linalg.eig(cov)
    idx = eigenVal.argsort()[::-1]
    eigenVal = eigenVal[idx]
    eigenVec = eigenVec[:,idx]
    return eigenVec