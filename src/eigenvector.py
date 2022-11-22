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
    return proj

# QR decomposition
def getQR(matrix):
    n = len(matrix)
    q = np.zeros((n,n))
    a = np.zeros((n,n))
    u = np.zeros((n,n))
    r = np.zeros((n,n))
    norm1 = None
    for i in range(n):
        a[i] = matrix.T[i]
        u[i] = a[i]
        for j in range(0, i):
            if (norm(u[j]) != 0):
                u[i] -= proj(u[j], a[i])
        norm1 = norm(u[i])
        if (norm1 != 0):
            q[i] = np.divide(u[i], norm1)
    q = np.multiply(q.T,-1)
    r1 = np.dot(q.T, matrix)
    r = np.triu(r1)
    return q, r

# Finding eigen with QR algorithm
def find_eigen(cov):
    a = cov
    n = len(cov)
    eVec = np.eye(n)
    count = 0
    while (not(np.allclose(a, np.triu(a), 0.0001))):
        # q,r = getQR(a)
        q,r = np.linalg.qr(a)
        a = np.dot(r,q)
        eVec = np.dot(eVec, q)
        count += 1
    e = [a[i][i] for i in range(len(cov))]
    eVec = np.absolute(eVec)
    return e, eVec

def find_eigenface(A, eVec):
    eig = np.dot(A, eVec)
    eig = eig.reshape((256*256))
    return eig