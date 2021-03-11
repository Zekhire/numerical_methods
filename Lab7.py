import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

lines = [line.rstrip('\n') for line in open('measurements4.txt')]

x = []
y = []
for i in range(len(lines)):
    split = lines[i].split()
    x.append(float(split[0]))
    y.append(float(split[1]))

print("x\n", x)
print("y\n", y)

T = 1.0
F = np.matrix(np.identity(4))
F[0, 2], F[1, 3] = T, T
G = np.transpose(np.matrix([[0, 0, 1.0, 0], [0, 0, 0, 1.0]]))
H = np.matrix([[1.0, 0, 0, 0], [0, 1.0, 0, 0]])

print("F\n", F)
print("G\n", G)
print("H\n", H)


P = 5.0*np.matrix(np.identity(4))
Q = 0.25*np.matrix(np.identity(2))
R = 2.0*np.matrix(np.identity(2))

print("P\n", P)
print("Q\n", Q)
print("R\n", R)




s_daszek = []
s_daszek.append(np.transpose(np.matrix([x[0], y[0], 0, 0])))
P = []
P.append(5*np.matrix(np.identity(4)))
z_daszek = []
z_daszek.append(np.matrix([0, 0]))
z = []
z.append(np.matrix([x[0], y[0]]))
e = []
e.append(np.matrix([0, 0, 0, 0]))
S = []
S.append(0)
K = []
K.append(0)
przew_x = []
przew_y = []
wyzn_x = []
wyzn_y = []

def Kalman_filter(t):
    for n in range(t):
        # Faza predykcji
        s_daszek.append(F*s_daszek[n])
        P.append(F*P[n]*np.transpose(F) + G*Q*np.transpose(G))
        z_daszek.append(H*s_daszek[n+1])

        przew_x.append(s_daszek[-1][0].item())
        przew_y.append(s_daszek[-1][1].item())
        if n < len(x)-1:
            # Faza innowacji
            z.append(np.transpose(np.matrix([x[n+1], y[n+1]])))
            e.append(z[n+1] - z_daszek[n+1])

            S.append(H*P[n+1]*np.transpose(H) + R)
            K.append(P[n+1]*np.transpose(H)*inv(S[n+1]))
            # Faza aktualizacji ﬁltru
            s_daszek[n+1] = s_daszek[n+1] + K[n+1]*e[n+1]

            wyzn_x.append(s_daszek[-1][0].item())
            wyzn_y.append(s_daszek[-1][1].item())

            P[n+1] = (np.identity(4) - K[n+1]*H)*P[n+1]

Kalman_filter(len(x) + 5)

blue = mpatches.Patch(color='blue', label='pomiar')
magenta = mpatches.Patch(color='magenta', label='wyznaczony')
red = mpatches.Patch(color='red', label='przewidywany')
plt.legend(handles=[blue, magenta, red])
plt.grid()

plt.plot(x, y, 'bx')
plt.plot(wyzn_x, wyzn_y, 'magenta')
plt.plot(przew_x, przew_y, 'r--')
plt.xlabel('x')
plt.ylabel('y')
plt.scatter(przew_x[-1], przew_y[-1], s=30, facecolors='none', edgecolors='r')
plt.show()