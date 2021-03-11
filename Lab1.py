import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.patches as mpatches


x = 0.5
a = math.pi/4
n = 10
rozw = list(range(n))
suma = []
bledy_bezwzgledne = []
bledy_wzgledne = []
pokaz = True

def rozwiniecie(n, x):
    lista = np.arange(1, n, 1)
    licznik = (x*math.log(a))**lista
    mianownik = np.cumprod(lista)
    wynik = licznik/mianownik
    suma = sum(wynik) + 1
    blad_bezwzgledny = abs(a ** x - suma)
    blad_wzgledny = blad_bezwzgledny * 100 / (a ** x)
    if pokaz:
        print("%s\t\t\t\t %s\t\t\t\t\t %s\t\t\t\t %s" % (n, suma, blad_bezwzgledny, blad_wzgledny))
    return suma

print("rząd\t\t\t\t suma\t\t\t\t\t\t błąd bwzg\t\t\t\t błąd wzg")
for i in range(1,n+1):
    rozwiniecie(i, x)


pokaz=False
def wykres():
    Y1 = []
    Y2 = []
    Y3 = []
    X=np.arange(0,1,0.01)
    Y=a**X
    iks = np.arange(0, 1, 0.01)
    for bu in iks:
        Y1.append(rozwiniecie(2, bu))
        Y2.append(rozwiniecie(5, bu))
        Y3.append(rozwiniecie(10, bu))

    red_patch = mpatches.Patch(color='red', label='N=2')
    blue_patch = mpatches.Patch(color='blue', label='N=5')
    green_patch = mpatches.Patch(color='green', label='N=10')
    magenta_patch = mpatches.Patch(color='magenta', label='orginal')
    plt.legend(handles=[red_patch, blue_patch, green_patch, magenta_patch])

    plt.plot(X, Y1, color='red')
    plt.plot(X, Y2, color='blue')
    plt.plot(X, Y3, color='green')
    plt.plot(X, Y, color='magenta')
    plt.show()

wykres()