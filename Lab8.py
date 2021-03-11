import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

lines = [line.rstrip('\n') for line in open('data19.txt')]

x = []
y = []
for i in range(len(lines)):
    split = lines[i].split()
    x.append(float(split[0]))
    y.append(float(split[1]))

print("x\n", x)
print("y\n", y)


# def wielomian_interpolacyjny_Newtona2(x, y, N):
#     x_wiN = np.linspace(x[0], x[-1], N)
#     y_wiN = []
#     j = 0
#     for i in range(len(x)-1):
#         while ((j<N) and (x_wiN[j] <= x[i+1])):
#             y_wiN.append(y[i]+((y[i+1]-y[i])/(x[i+1]-x[i])*(x_wiN[j]-x[i])))
#             j += 1
#     return x_wiN, y_wiN



def unormowane_roznice_skonczone(x, y, i, j, bn = []):
    if len(y) == 1:
        if i == 0:
            bn.append(y[0])
        return y[0], bn
    else:
        y1, bn = unormowane_roznice_skonczone(x[0:len(x) - 1], y[0:len(y) - 1], i, j - 1, bn)   #f[xn-1, ..., x2, x1]
        y2, _ = unormowane_roznice_skonczone(x[1:len(x)], y[1:len(y)], i + 1, j)  # f[xn, xn-1, ..., x2]
        x1 = x[0]
        x2 = x[len(x)-1]
        b = (y2 - y1) / (x2 - x1)
        if i == 0:
            bn.append(b)
        return b, bn

def wielomian_interpolacyjny_Newtona(x, y, N):
    x_wiN = np.linspace(x[0], x[-1], N)
    y_wiN = []
    _, b = unormowane_roznice_skonczone(x, y, 0, len(x))
    print(b[10])
    for i in range(len(x_wiN)):
        tempi = 0
        for j in range(len(x)):
            tempj = b[j]
            for k in range(j):
                tempj *= x_wiN[i] - x[k]
            tempi += tempj
        y_wiN.append(tempi)
    return x_wiN, y_wiN


# def funkcja_sklejana_drugiego_rzedu(x, y, N):
#     x_fsdr = np.linspace(x[0], x[-1], N)
#     y_fsdr = []
#     A = []
#     B = []
#     st = 2 * (len(x) - 1)
#
#     for i in range((len(x)-1)):
#         A_row = list(np.zeros(st))
#         A_row[2*i] =    x[i+1] - x[i]        # bi
#         A_row[2*i+1] = (x[i+1] - x[i])**2     # ci
#         A.append(A_row)
#         B.append(y[i + 1] - y[i])
#
#     for i in np.arange(len(x)-2):
#         A_row = list(np.zeros(st))
#         A_row[2*i] = 1
#         A_row[2*i+1] = 2*(x[i+1]-x[i])
#         A_row[2*(i+1)] = -1
#         A.append(A_row)
#         B.append(0)
#
#     A_row = list(np.zeros(st))
#     A_row[1] = 1
#     A.append(A_row)
#     B.append(0)
#
#     B = np.transpose(np.array(B))
#     X = np.linalg.solve(A, B)
#     j = 0
#     for i in range(len(x)-1):
#         while ((j<N) and (x_fsdr[j] <= x[i+1])):
#             y_fsdr.append(y[i]+X[2*i]*(x_fsdr[j]-x[i])+X[2*i+1]*((x_fsdr[j]-x[i])**2))
#             j += 1
#     return x_fsdr, y_fsdr


def funkcja_sklejana_trzeciego_rzedu(x, y, N):
    x_fstr = np.linspace(x[0], x[-1], N)
    y_fstr = []
    A = []
    B = []

    A_row = np.zeros(len(x))
    A_row[0] = 1
    A.append(A_row)
    B.append(0)
    for i in range(len(x)-2):
        A_row = np.zeros(len(x))
        A_row[i] = x[i + 1] - x[i]
        A_row[i + 2] = x[i + 2] - x[i + 1]
        A_row[i + 1] = 2*(A_row[i] + A_row[i+2])
        A.append(A_row)
        B.append(3 * (((y[i + 2] - y[i + 1]) / (x[i + 2] - x[i + 1])) - ((y[i + 1] - y[i]) / (x[i + 1] - x[i]))))
    A_row = np.zeros(len(x))
    A_row[-1] = 1
    A.append(A_row)
    B.append(0)
    B = np.transpose(np.array(B))
    c = np.linalg.solve(A, B)

    b = []
    d = []
    for i in range(len(x)-1):
        b.append((y[i+1]-y[i])/(x[i+1]-x[i]) - (x[i+1]-x[i])*(2*c[i] + c[i+1])/3)
        d.append((c[i + 1] - c[i]) / (3 * (x[i + 1] - x[i])))
    j = 0
    for i in range(len(x)-1):
        while ((j<N) and (x_fstr[j] <= x[i+1])):
            y_fstr.append(y[i]+b[i]*(x_fstr[j]-x[i])+c[i]*((x_fstr[j]-x[i])**2)+d[i]*((x_fstr[j]-x[i])**3))
            j += 1
    return x_fstr, y_fstr

x_wiN, y_wiN = wielomian_interpolacyjny_Newtona(x, y, 1000)
#x_fsdr, y_fsdr = funkcja_sklejana_drugiego_rzedu(x, y, 1000)
x_fstr, y_fstr = funkcja_sklejana_trzeciego_rzedu(x, y, 1000)

green = mpatches.Patch(color='green', label='punkty pomiarowe')
blue = mpatches.Patch(color='blue', label='wielomian interpolacyjny Newtona')
#orange = mpatches.Patch(color='orange', label='funkcja sklejana drugiego rzedu')
red = mpatches.Patch(color='red', label='funkcja sklejana trzeciego rzedu')
plt.legend(handles=[green, blue, red])
plt.grid()



plt.plot(x_wiN, y_wiN, 'blue')
#plt.plot(x_fsdr, y_fsdr, 'orange')
plt.plot(x_fstr, y_fstr, 'red')
plt.scatter(x, y, facecolor='green')
plt.xlim(x[0], x[-1])
plt.show()