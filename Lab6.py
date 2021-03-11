import matplotlib.pyplot as plt
import scipy.optimize
import numpy as np
import scipy
import matplotlib.patches as mpatches



lines = [line.rstrip('\n') for line in open('data4.txt')]

t = []
y = []
for i in range(len(lines)):
    split = lines[i].split()
    t.append(float(split[0]))
    y.append(float(split[1]))

print("t = ", t)
print("y = ", y)


def step_response(t, k, tau, zeta, tauz):
    wn = 1 / tau
    w0 = wn * np.sqrt(1 - zeta ** 2)
    alfa = np.arctan(np.sqrt(1 - zeta ** 2) / zeta)
    # Odpowiedź impulsowa
    g = (wn * (np.e ** (-zeta * wn * t)) * np.sin(w0 * t) / np.sqrt(1 - zeta ** 2))
    # Odpowiedź skokowa
    h = (1 - (np.e ** (-zeta * wn * t)) * np.sin(w0 * t + alfa) / np.sqrt(1 - zeta ** 2))
    #h = (1 - (np.e ** (-zeta * wn * t)) * np.cos(w0 * t) + zeta * np.sin(w0 * t) / np.sqrt(1 - zeta ** 2))
    return k * (tauz*g + h)


def minimal_value(par):
    suma = 0
    for i in range(len(t)):
        suma += (y[i] - step_response(t[i], par[0], par[1], par[2], par[3]))**2
    return suma

t = np.array(t)
y = np.array(y)

#       |'  k    '|
# p =   |   tau   |
#       |   zeta  |
#       |,  tauz ,|

p = scipy.optimize.fmin(minimal_value, np.array([5, 2, 0.8, 2]))

print("\n")
print("Znalezione wartości")
print("k = ", p[0])
print("τ = ", p[1])
print("ζ = ", p[2])
print("τz = ", p[3])



plt.figure(figsize=(12, 6))
plt.plot(t, y)
plt.plot(t, step_response(t, p[0], p[1], p[2], p[3]), 'r')
blue_patch = mpatches.Patch(label='Dane pomiarowe')
red_patch = mpatches.Patch(color='red', label='Regresja nieliniowa')
plt.legend(handles=[blue_patch, red_patch])
plt.xlim((t[0], t[len(t)-1]))
plt.xlabel('czas')
plt.ylabel('wartość')
plt.grid()
plt.show()