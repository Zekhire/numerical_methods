import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd
pd.options.display.float_format = '{:,.15f}'.format

a = math.pi/4
x = 0.5
h = 0.4
n = 20
przyrost = np.arange(0, n, 1)
przyrost = abs(h/(5.0**przyrost))

argument = np.ones(n)*x
argument_plus = argument + przyrost
argument_minus = argument - przyrost

pochodna_num = ((a**argument_plus) - (a**argument_minus))/(2*przyrost)
pochodna_mat = (a**x)*math.log(a)
blad_prawdziwy = abs((pochodna_num - pochodna_mat))

print(pd.DataFrame({'przyrost': przyrost, 'wartość pochodnej': pochodna_num, 'błąd': blad_prawdziwy}))
print('\n')
print("h o optymalnej wartości błędu ma wartość: %s" % przyrost[np.argmin(blad_prawdziwy)])

plt.plot(przyrost, blad_prawdziwy, 'mo')
plt.xscale("log")
plt.yscale("log")
plt.show()
