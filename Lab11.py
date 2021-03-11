import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def uklad_rownan(t, x, y, z):
    xprim = -10*x + 10*y
    yprim = 28*x - y - x*z
    zprim = (-8/3)*z + x*y
    return xprim, yprim, zprim

def ploting(t, Y, string):
    plt.plot(t, Y)
    plt.ylabel(string)
    plt.xlabel('t')
    plt.ylim(min(Y), max(Y) + 1)
    plt.xlim(min(t), max(t))
    plt.grid()
    plt.show()

def RK4(t0, tk, h, x0, y0, z0):
    t = [t0]
    x = [x0]
    y = [y0]
    z = [z0]
    while t[-1] < tk:
        k11, k12, k13 = uklad_rownan(t[-1], x[-1], y[-1], z[-1])
        k21, k22, k23 = uklad_rownan(t[-1] + h / 2, x[-1] + k11 * h / 2, y[-1] + k12 * h / 2, z[-1] + k13 * h / 2)
        k31, k32, k33 = uklad_rownan(t[-1] + h / 2, x[-1] + k21 * h / 2, y[-1] + k22 * h / 2, z[-1] + k23 * h / 2)
        k41, k42, k43 = uklad_rownan(t[-1] + h, x[-1] + k31 * h, y[-1] + k32 * h, z[-1] + k33 * h)
        x.append(x[-1] + (1 / 6) * (k11 + 2 * (k21 + k31) + k41) * h)
        y.append(y[-1] + (1 / 6) * (k12 + 2 * (k22 + k32) + k42) * h)
        z.append(z[-1] + (1 / 6) * (k13 + 2 * (k23 + k33) + k43) * h)
        t.append(t[-1] + h)
    return t, x, y, z

t0 = 0
tk = 25
h = 0.03125
x0 = 5
y0 = 5
z0 = 5

t, x, y, z = RK4(t0, tk, h, x0, y0, z0)

with pd.option_context('display.max_rows', None, 'display.max_columns', 6):
    print(pd.DataFrame({'t': t, 'x': x, 'y': y, 'z': z}))


ploting(t, x, 'x')
ploting(t, y, 'y')
ploting(t, z, 'z')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, 'b')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()