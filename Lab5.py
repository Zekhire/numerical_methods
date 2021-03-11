import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from numpy.linalg import inv


def step(A, B, C, D, N):
    n = []
    Y = np.zeros(N)
    X = B*0
    u = 1
    for i in range(N):
        n.append(i)
        X0 = X
        X    = A*X0 + B*u
        Y[i] = C*X0 + D*u
    return n, Y


def Riccati(c1, c2, A, B):
    Q = c1*np.identity(3)
    R = c2
    P = 0*np.identity(3)
    for v in range(10):
        P = Q + np.transpose(A) * (P - (P*B*inv(R + np.transpose(B)*P*B)) * np.transpose(B) * P) * A
    return Q, R, P


def ploting(ax, n, Y, string):
    ax.stem(n, Y, 'b', markerfmt='bo', linefmt='b--')
    markerline, stemlines, baseline = ax.stem(n, np.ones(len(n)), 'r', markerfmt='ro', linefmt='r-.')
    plt.setp(baseline, color='black', linewidth=2)
    ax.set_title(string)
    ax.legend(handles=[mpatches.Patch(color='red', label='step'), mpatches.Patch(color='blue', label='response')])
    ax.grid()


#   4.
#                    z^2 + z + 1
#   G(z) = -------------------------------
#           z^3 - 3.15z^2 + 2.525z - 0.45



fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(13, 5))
A = np.matrix([[3.15, -2.525, 0.45], [1, 0, 0], [0, 1, 0]])
B = np.transpose(np.matrix([1, 0, 0]))
C = np.matrix([1, 1, 1])
D = np.matrix([0])
print("Model stanowy")
print("Macierz A\n", A)
print("Macierz B\n", B)
print("Macierz C\n", C)
print("Macierz D\n", D)

N = 30
n, Y = step(A, B, C, D, N)
ploting(ax1, n, Y, 'Odpowiedź układu bez LQR')                              # <- układ nie jest stabilny - odpowiedź w czasie->inf zmierza do inf

c1 = 1
c2 = 1
Q, R, P = Riccati(c1, c2, A, B)
print("\nMacierz P\n", P)
F = (inv(R + np.transpose(B) * P * B)) * np.transpose(B) * P * A
print("Macierz F\n", F)
n, Y = step(A - B*F, B, C, D, N)
ploting(ax2, n, Y, 'Odpowiedź układu z LQR\n dla c1={0}, c2={1}'.format(c1, c2))

#c1 = 0.001
#c2 = 3
c1 = 3
c2 = 0.001
Q, R, P = Riccati(c1, c2, A, B)
print("\nMacierz P z innymi parametrami c1 i c2\n", P)
F = (inv(R + np.transpose(B) * P * B)) * np.transpose(B) * P * A
print("Macierz F z innymi parametrami c1 i c2\n", F)
n, Y = step(A - B*F, B, C, D, N)
ploting(ax3, n, Y, 'Odpowiedź układu z LQR\n dla c1={0}, c2={1}'.format(c1, c2))        # <- parametry c1 i c2 wpływają na wzmocnienie układu i na stałą czasową
plt.show()
