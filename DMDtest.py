import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Define time and space discretizations
x = np.linspace(-10, 10, 400)
tSpan = np.linspace(0, 4 * np.pi, 200)
dt = tSpan[2] - tSpan[1]
Xgrid,T = np.meshgrid(x, tSpan)

# Create two spatio-temporal patterns
f1 = np.multiply(1/np.cosh(Xgrid + 3), np.exp((2.3j)*T))
f2 = np.multiply(1/np.cosh(Xgrid), np.tanh(Xgrid), 2*np.exp(2.8j*T))

## Combine signals and make data matrix
Data = (f1 + f2).T

## Visualize f1, f2, f
fig = plt.figure()
axes = fig.gca(projection='3d')
axes.view_init(30, 70)
surf = axes.plot_surface(Xgrid, T, np.real(f2), rstride=1, cstride=1, cmap='viridis', edgecolor='none', antialiased=True)
plt.show()

""" Performing DMD on data """

# create DMD input-output matrices from multidimensional subarrays
X1 = Data[:, :-1]
X2 = Data[:, 1:]

# Singular value decomposition and rank-2 truncation
U, Sig, V = np.linalg.svd(X1, full_matrices=False)

r = 2
U_r = U[:, :r]
Sig_r = np.diag(Sig)[:r, :r]
V_r = V.conj().T[:, :r]

# build A tilde
Atilde = np.dot(np.dot(np.dot(U_r.conj().T, X2), V_r), np.linalg.inv(Sig_r))
D, W = np.linalg.eig(Atilde)

# build DMD modes
Phi = np.dot(np.dot(np.dot(X2, V_r), np.linalg.inv(Sig_r)), W)

# DMD Spectra

# Lambda = np.diag(D)
# Omega = np.log(Lambda)/dt

# Compute DMD solution
b = np.dot(np.linalg.pinv(Phi), Data[:, 0])
Psi = np.zeros([r, len(tSpan)], dtype='complex')
for i, _t in enumerate(tSpan):
    Psi[:,i] = np.multiply(np.power(D, _t / dt), b)

# compute DMD reconstruction
X_DMD = np.dot(Phi, Psi)

plt.figure()
plt.plot(Phi)
plt.show()
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# ax.view_init(30, 70)
# # surf = ax.plot_surface(Xgrid,T,linewidth=0, antialiased=False)
# surf = ax.plot_surface(Xgrid, T, np.real(f2), Linewidth =1, rstride=1, cstride=1, cmap='viridis', edgecolor='none', antialiased=True)
# plt.show()