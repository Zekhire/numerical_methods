import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.patches as mpatches
pd.options.display.float_format = '{:,.7f}'.format


x = np.linspace(-6, 5, 100000)
y1 = x*x - 2*x + 0.5
y2 = -(x*x)/(7 + 2*x)
plt.ylim((-6, 30))
plt.grid(True)
plt.plot(x, y1, color='green')
plt.plot(x, y2, color='magenta')
green = mpatches.Patch(color='green', label='f1(x)')
magenta = mpatches.Patch(color='magenta', label='f2(x)')
plt.legend(handles=[green, magenta])
plt.ylabel('y')
plt.xlabel('x')
plt.show()
# Liczba pierwiastków: 3
# Współrzędne pierwiastka 1: (-3.82387, 22.7448)
# Współrzędne pierwiastka 2: (0.304013, -0.0126857)
# Współrzędne pierwiastka 3: (1.51865, -0.229618)


n = 10

# Metoda Iteracyjnego Podstawiania
def MIP(x, y, n):
    y_rozw = []
    x_rozw = []
    y_rozw.append(y)
    x_rozw.append(x)
    for i in range(n):
        x = (-x*x - 7*y) / (2 * y)
        x_rozw.append(x)
        y = x*x - 2*x + 0.5
        y_rozw.append(y)

    return x_rozw, y_rozw

print("Wyniki dla Metody Iteracyjnego Podstawiania")
MIP_x_rozw1, MIP_y_rozw1 = MIP(-4,     24, n)
MIP_x_rozw2, MIP_y_rozw2 = MIP(0.4, -0.01, n)
MIP_x_rozw3, MIP_y_rozw3 = MIP(2,    -0.3, n)
print(pd.DataFrame({'x1': MIP_x_rozw1, 'y1': MIP_y_rozw1, ' ': '|', 'x2': MIP_x_rozw2, 'y2': MIP_y_rozw2, '': '|', 'x3': MIP_x_rozw3, 'y3': MIP_y_rozw3}), '\n')


# y - x^2 + 2*x = 0.5
def rown1_pochodna_po_x(x, y):
    return -2*x +2

def rown1_pochodna_po_y(x, y):
    return 1

# x^2 + 7*y + 2*xy = 0
def rown2_pochodna_po_x(x, y):
    return 2*x + 2*y

def rown2_pochodna_po_y(x, y):
    return 7 + 2*x

def funk1(x, y):
    return y - x*x + 2*x - 0.5

def funk2(x, y):
    return x*x + 7*y + 2*x*y

def MNR(x, y, n):
    y_rozw = []
    x_rozw = []
    y_rozw.append(y)
    x_rozw.append(x)
    for i in range(n):
        df1x = rown1_pochodna_po_x(x, y)
        df1y = rown1_pochodna_po_y(x, y)
        df2x = rown2_pochodna_po_x(x, y)
        df2y = rown2_pochodna_po_y(x, y)
        jakobian = df1x*df2y - df1y*df2x
        x = x - (funk1(x, y)*df2y - funk2(x, y)*df1y)/jakobian
        x_rozw.append(x)
        y = y - (funk2(x, y)*df1x - funk1(x, y)*df2x)/jakobian
        y_rozw.append(y)

    return x_rozw, y_rozw

print("Wyniki dla Metody Newtona-Raphsona")
MNR_x_rozw1, MNR_y_rozw1 = MNR(-4,     24, n)
MNR_x_rozw2, MNR_y_rozw2 = MNR(0.4, -0.01, n)
MNR_x_rozw3, MNR_y_rozw3 = MNR(2,    -0.3, n)
print(pd.DataFrame({'x1': MNR_x_rozw1, 'y1': MNR_y_rozw1, ' ': '|', 'x2': MNR_x_rozw2, 'y2': MNR_y_rozw2, '': '|', 'x3': MNR_x_rozw3, 'y3': MNR_y_rozw3}), '\n')