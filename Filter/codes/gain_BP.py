import numpy as np

# Given parameters
s1 = -0.3913 - 0.4156j
s2 = -0.3913 + 0.4156j
s3 = -0.1621 + 1.0033j
s4 = -0.1621 - 1.0033j
epsilon = 0.4
Omega_Lp = 1
# Define denominator polynomial
den = np.poly([s1, s2, s3, s4])

# Define frequency range
w = np.arange(-2, 2.01, 0.01)

num = 0.3125

# Define parameters for transformation
B = 0.0884
Omega0 = 0.352

# Perform transformation to get s_L
s_L = (1j * 0.3111)**2 + Omega0**2
s_L /= B * (1j * 0.3111)

H = num / np.polyval(den, s_L)
print(1 / abs(H))
