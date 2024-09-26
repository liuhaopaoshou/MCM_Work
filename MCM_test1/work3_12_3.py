import scipy.integrate as integrate
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def integrand(z, y, x):
    return z

# 定义区域Ω的边界
def z_lower(x, y):
    return x**2 + y**2

def z_upper(x, y):
    return 4

def y_lower(x):
    return -np.sqrt(4 - x**2)

def y_upper(x):
    return np.sqrt(4 - x**2)

result, error = integrate.tplquad(integrand, -2, 2, y_lower, y_upper, z_lower, z_upper)
print("Integral (3) =", result)

x = np.linspace(-2, 2, 400)
y = np.linspace(-2, 2, 400)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, alpha=0.5, rstride=100, cstride=100)
ax.plot_surface(X, Y, 4*np.ones_like(Z), alpha=0.5)
ax.set_title(r'区域 $\Omega$')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
