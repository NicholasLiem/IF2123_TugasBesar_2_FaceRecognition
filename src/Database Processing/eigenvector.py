import numpy as np

# Fungsi mencari nilai eigen dengan algoritma QR #
def eigen_qr(cov):
    a = cov
    for i in range(256):
        q, r = np.linalg.qr(a)
        a = np.dot(r, q)
    e = [a[i][i] for i in range(256)]
    return e
    