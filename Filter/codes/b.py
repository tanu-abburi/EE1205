import numpy as np
import matplotlib.pyplot as plt

# Given parameters
s1 = -0.3913 - 0.4156j
s2 = -0.3913 + 0.4156j
s3 = -0.1621 + 1.0033j
s4 = -0.1621 - 1.0033j
epsilon = 0.4
Omega_Lp = 1

# Generate the denominator polynomial
den = np.poly([s1, s2, s3, s4])

# Define frequency range
w = np.arange(0, 2.01, 0.01)

# Read precomputed values of C_N from file
cn_values = np.loadtxt("cn_values.txt")

# Extract Omega_L values and corresponding C_N values
Omega_L_values = cn_values[:, 0]
c_N_values = cn_values[:, 1]

# Calculate |Ha(jOmega_L)| using precomputed c_N values
x = w / Omega_Lp
c_N_interpolated = np.interp(x, Omega_L_values, c_N_values)
Ha_values = 1 / np.sqrt(1 + epsilon**2 * c_N_interpolated**2)

# Plot magnitude response for epsilon = 0.5
plt.figure()
plt.plot(w, Ha_values, '*', label='Design')

G_LP = 0.3125
num = G_LP

# Calculate magnitude response for epsilon = 0.5
s = 1j * w
H = num / np.polyval(den, s)
magnitude = np.abs(H)

# Plot magnitude response for epsilon = 0.5
plt.plot(w, magnitude, label='Specification')

plt.title('Design vs Specification')
plt.xlabel('Analog Frequency ($\Omega$)')
plt.ylabel('|H_{a,LP}($\Omega$)|')
plt.legend()
plt.grid(True)
plt.ylim(0, 1.1)  # Set the y-axis limits from 0 to 2
plt.savefig("Design_vs_Specification.png")

