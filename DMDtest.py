import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


# Define time and space discretizations
x = np.linspace(-10, 10, 100)
t = np.linspace(0, 4*np.pi, 50)
dt = t[2] - t[1]
Xgrid,T = np.meshgrid(x, t)

# Create two spatio-temporal patterns
f1 = np.multiply(1/np.cosh(Xgrid + 3), np.exp((2.3j)*T))
f2 = np.multiply(1/np.cosh(Xgrid), np.tanh(Xgrid), 2*np.exp(2.8j*T))
# f3 = multiply(5*multiply(1/cosh(Xm/2), tanh(Xm/2)), 2*exp((0.1+2.8j)*Tm))

## Combine signals and make data matrix
Data = (f1 + f2).T

## Visualize f1, f2, f
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.view_init(30, 70)
# Plot the surface.
# surf = ax.plot_surface(Xgrid,T,linewidth=0, antialiased=False)
surf = ax.plot_surface(Xgrid, T, np.real(f2), Linewidth =1, rstride=1, cstride=1, cmap='viridis', edgecolor='none', antialiased=True)
plt.show()

""" Performing DMD on data """

# create DMD input-output matrices
X1 = Data[:,:-1]
X2 = Data[:,1:]
