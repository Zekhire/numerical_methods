import numpy as np
import matplotlib.pyplot as plt

dx, dy = 2, 2
Ta = 100
hprim = 0.05
sizex, sizey = 11, 11
unkn_sizex, unkn_sizey = sizex-2, sizey-2
A = np.zeros((unkn_sizex*unkn_sizey, unkn_sizex*unkn_sizey))  # 81 x 81
B = np.zeros((unkn_sizex*unkn_sizey, 1))
T = np.zeros((sizex, sizey))

for i in range(sizex):
    for j in range(sizey):
        if   i == 0:          T[i][j] = 400 - j*10
        elif i == sizex-1:    T[i][j] = 300 - j*10
        elif j == 0:          T[i][j] = 400 - i*10
        elif j == sizey-1:    T[i][j] = 300 - i*10

for i in range(unkn_sizey):
    for j in range(unkn_sizex):
        for z in range(unkn_sizex * unkn_sizey):
            if z % unkn_sizex == j:
                if (int)(z/unkn_sizex) == i:
                    B[i*unkn_sizex + j] = Ta
                    A[z][i*unkn_sizex + j] = 2/(dx*dx*hprim) + 2/(dy*dy*hprim) + 1
                    if T[i+1][j]   != 0:  B[i*unkn_sizex + j]     += T[i+1][j]/ (dx * dx * hprim)
                    else:                 A[z][i*unkn_sizex + j - 1]  = -1 / (dx * dx * hprim)
                    if T[i+1][j+2] != 0:  B[i*unkn_sizex + j]     += T[i+1][j+2]/ (dx * dx * hprim)
                    else:                 A[z][i*unkn_sizex + j + 1]  = -1 / (dx * dx * hprim)
                    if T[i][j+1]   != 0:  B[i*unkn_sizex + j]     += T[i][j+1]/ (dy * dy * hprim)
                    else:                 A[z][(i-1)*unkn_sizex + j]  = -1 / (dy * dy * hprim)
                    if T[i+2][j+1] != 0:  B[i*unkn_sizex + j]     += T[i+2][j+1]/ (dy * dy * hprim)
                    else:                 A[z][(i+1)*unkn_sizex + j]  = -1 / (dy * dy * hprim)

print("macierz A:")
print(A)
print("macierz B:")
print(B)
X = np.linalg.solve(A, B)
print("macierz X:")
print(X)
for i in range(unkn_sizex):
    for j in range(unkn_sizey):
        T[i+1][j+1] = X[i*9+j]

np.set_printoptions(precision=1)
print("macierz T:")
print(T)
plt.imshow(T, cmap='hot_r')
plt.show()