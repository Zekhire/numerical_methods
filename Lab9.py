import pandas as pd
import math
print("funkcja\nf = 0.02721x^4 + 0.5415x^3 - 0.1211x^2 + 4.27x - 2.21")
print("\n")
x_4 = 0.02721
x_3 = 0.5415
x_2 = -0.1211
x_1 = 4.27
x_0 = -2.21
a = -20
b = 5

metoda = []
wynik = []

def funkcja(x, x_4, x_3, x_2, x_1, x_0):
    return ((x_4*x**4) + (x_3*x**3) + (x_2*x**2) + (x_1*x) + x_0)

def calka(x, x_4, x_3, x_2, x_1, x_0):
    return x_4 / 5 * x ** 5 + x_3 / 4 * x ** 4 + x_2 / 3 * x ** 3 + x_1 / 2 * x ** 2 + x_0 / 1 * x

def metodaAnalityczna(a, b, x_4, x_3, x_2, x_1, x_0):
    wynik_a = calka(a, x_4, x_3, x_2, x_1, x_0)
    wynik_b = calka(b, x_4, x_3, x_2, x_1, x_0)
    return wynik_b - wynik_a


print('Współczynniki wielomianu wynikowego')
print(pd.DataFrame({'Współczynnik ': ["x^5", "x^4", "x^3", "x^2", "x^1", "x^0"],
                    'wartość ':      [x_4/5, x_3/4, x_2/3, x_1/2, x_0/1, 0]}))

print("\n")

metoda.append("Analityczny")
wynik.append(metodaAnalityczna(a, b, x_4, x_3, x_2, x_1, x_0))

c0 = 5 / 9
c1 = 8 / 9
c2 = 5 / 9
x0 = - math.sqrt(3 / 5)
x1 = 0
x2 = math.sqrt(3 / 5)

dx = (b - a) / 2

def metodaTrapezow(a, b, n):
    h = (b - a) / n
    x = a
    suma = funkcja(x, x_4, x_3, x_2, x_1, x_0)
    for i in range(n-1):
        x += h
        suma += 2 * funkcja(x, x_4, x_3, x_2, x_1, x_0)
    return (suma + funkcja(b, x_4, x_3, x_2, x_1, x_0))*h/2


def metodaRomberga(a, b, wynikAnalityczny, kryterium):
    posrednie = []
    i = 0
    while(True):
        posrednie_i = []
        posrednie_i.append(metodaTrapezow(a, b, 2 ** i))
        for j in range(i):
            posrednie_i.append((4 ** (j + 1) * posrednie_i[j] - posrednie[i-1][j]) / (4 ** (j + 1) - 1))
        posrednie.append(posrednie_i)
        wynikRomberg = posrednie[-1][-1]
        if((abs((wynikRomberg - wynikAnalityczny)/wynikAnalityczny))*100 < kryterium):
            return posrednie
        i += 1

kryterium = 0.2
wynikRomberg = metodaRomberga(a, b, wynik[0], kryterium)
print("Wyniki posrednie metody Romberga")
for i in range(len(wynikRomberg)):
    metoda.append("Romberg" + str(i + 1))
    wynik.append(wynikRomberg[i][-1])
    print(pd.DataFrame({'Romberg' + str(i + 1): wynikRomberg[i]}))
    print("\n")


def trzyPunktowaKwadraturaGaussa(t):
    x = ((b + a) + (b - a) * t) / 2
    f = funkcja(x, x_4, x_3, x_2, x_1, x_0) * dx
    return f

metoda.append("Trzypunktowa Kwadratura Gaussa")
wynikGauss = (c0*trzyPunktowaKwadraturaGaussa(x0) +
              c1*trzyPunktowaKwadraturaGaussa(x1) +
              c2*trzyPunktowaKwadraturaGaussa(x2))
wynik.append(wynikGauss)


print("Wyniki całki")
print(pd.DataFrame({'Metoda': metoda, 'Wynik': wynik}))
