import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# równanie różniczkowe
# dy/dt = -3yt^2 + 3y;   y(0) = 3

# rozwiązanie analityczne
# y = 3e^(3t-t^3)

t0 = 0
tk = float(input("Wpisz czas końcowy tk: "))
y0 = 3
n = 100


def metodaEulera(t0, tk, n, y0):
    y = []
    y.append(y0)
    t = []
    t.append(t0)
    dt = (tk - t0) / n
    for i in range(n):
        y.append(y[-1] + (-3 * y[-1] * (t[-1] ** 2 - 1)) * dt)
        t.append(t[-1] + dt)
    return y, t


def metodaHeuna(t0, tk, n, y0):
    y = []
    y.append(y0)
    t = []
    t.append(t0)
    dt = (tk - t0) / n
    for i in range(n):
        yprimi = (-3 * y[-1] * (t[-1] ** 2 - 1))
        y0iplus1 = y[-1] + yprimi*dt                # Metoda Eulera
        t.append(t[-1] + dt)
        yprimiplus1 = (-3 *y0iplus1 * (t[-1] ** 2 - 1))
        yprimzkreska = (yprimi + yprimiplus1)/2
        y.append(y[-1]+yprimzkreska*dt)
    return y, t


def metodaPunktuSrodkowego(t0, tk, n, y0):
    y = []
    y.append(y0)
    t = []
    t.append(t0)
    dt = (tk - t0) / n
    for i in range(n):
        yiplus1przez2 = y[-1] + (-3 * y[-1] * (t[-1] ** 2 - 1)) * dt/2
        tiplus1przez2 = t[-1] + dt/2
        y.append(y[-1] + (-3 * yiplus1przez2 * (tiplus1przez2 ** 2 - 1)) * dt)
        t.append(t[-1] + dt)
    return y, t

yE, t = metodaEulera(t0, tk, n, y0)
yH, _ = metodaHeuna(t0, tk, n, y0)
yP, _ = metodaPunktuSrodkowego(t0, tk, n, y0)
y=[]

for ti in t:
    y.append(3*np.e**(+3*ti-(ti**3)))

with pd.option_context('display.max_rows', None, 'display.max_columns', 6):  # more options can be specified also
    print(pd.DataFrame({'t': t, 'analityczny': y, 'Euler': yE, 'Heun': yH, 'punkt środkowy':yP}))


plt.plot(t, y, color='blue')
plt.plot(t, yE, color='red')
plt.plot(t, yH, color='green')
plt.plot(t, yP, color='magenta')
blue = mpatches.Patch(color='blue', label='metoda analityczna')
red = mpatches.Patch(color='red', label='metoda Eulera')
green = mpatches.Patch(color='green', label='metoda Heuna')
magenta = mpatches.Patch(color='magenta', label='metoda punktu środkowego')
plt.legend(handles=[blue, red, green, magenta])
plt.ylabel('y')
plt.xlabel('t')
plt.grid()
plt.show()