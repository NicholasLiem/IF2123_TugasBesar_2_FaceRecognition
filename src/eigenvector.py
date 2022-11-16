import numpy as np

# Fungsi mencari nilai eigen dengan algoritma QR #
# The norm of a vector
def norm(vector):
    norm = 0
    for i in vector:
        norm += (i ** 2)
    norm = norm ** (1/2)
    return norm

# Projection of u on a
def proj(u,a):
    proj = 0
    norm2 = norm(u) ** 2
    for i in range(len(u)):
        proj += (u[i] * a[i])
    proj /= norm2
    proj = np.multiply(proj, u)
    print(proj)
    return proj

# QR decomposition
def getQR(matrix):
    n = len(matrix)
    q = np.zeros((n,n))
    a = np.zeros((n,n))
    u = np.zeros((n,n))
    for i in range(n):
        a[i] = matrix.T[i]
        u[i] = a[i]
        for j in range(0, i):
            if (norm(u[j]) != 0):
                u[i] -= proj(u[j], a[i])
        print(u[i])
        if (norm(u[i]) != 0):
            q[i] = np.divide(u[i], norm(u[i]))
        else:
            q[i] = 0
    q = q.T
    r = np.dot(q.T, matrix)
    return q, r

# Checking for upper triangular matrix
def isTriangle(matrix):
    triangle = True
    for i in range(1, len(matrix)):
        for j in range(i):
            if (matrix[i][j] > 0.0001 or matrix[j][i] < -0.0001):
                triangle = False
    return triangle

# Finding eigen with QR algorithm
def find_eigen(cov):
    a = cov
    triangle = False
    n = len(cov)
    eVec = np.eye(n)
    while (not(triangle)):
        q,r = np.linalg.qr(a)
        triangle = isTriangle(np.dot(r, q))
        if (not(triangle)):
            a = np.dot(r, q)
            eVec = np.dot(eVec, q)
    e = [a[i][i] for i in range(len(cov))]
    return e, eVec

def find_eigen2(A, eVec):
    eig = np.dot(A,eVec[0])
    return eig

def sort_eigen(cov):
    eigenVal, eigenVec  = np.linalg.eig(cov)
    idx = eigenVal.argsort()[::-1]
    eigenVal = eigenVal[idx]
    eigenVec = eigenVec[:,idx]
    return eigenVec