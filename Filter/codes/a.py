import numpy as np
import matplotlib.pyplot as plt

# Given parameters
epsilons = [0.337, 0.45, 0.55, 0.61]

# Read precomputed values of C_N from file
cn_values = np.loadtxt("cn_values.txt")

# Extract Omega_L values and corresponding C_N values
Omega_L_values = cn_values[:, 0]
c_N_values = cn_values[:, 1]

# Value of order of filter
N = 4

# Tolerance for passband and stopband
passband_tolerance = 0.15
stopband_tolerance = 0.15

# Calculate Ha(jOmega_L) for different Omega_L values
Ha_values = np.zeros((len(epsilons), len(Omega_L_values)))
for j, epsilon in enumerate(epsilons):
    Ha_values[j, :] = 1 / np.sqrt(1 + epsilon**2 * c_N_values**2)

# Plotting
plt.figure()
for j, epsilon in enumerate(epsilons):
    plt.plot(Omega_L_values, np.abs(Ha_values[j, :]), label=f'Epsilon = {epsilon}')

# Draw passband and stopband
passband_lower_limit = 1 - passband_tolerance
stopband_upper_limit = stopband_tolerance

# Passband
passband_x = [0, 1, 1, 0]
passband_y = [passband_lower_limit, passband_lower_limit, 1, 1]
plt.fill(passband_x, passband_y, 'g', alpha=0.3, edgecolor='none')

# Stopband
stopband_x = [1.442, 2, 2, 1.442]
stopband_y = [0, 0, stopband_upper_limit, stopband_upper_limit]
plt.fill(stopband_x, stopband_y, 'r', alpha=0.3, edgecolor='none')

plt.xlabel('$\Omega$_L')
plt.ylabel('|Ha LP($\Omega$)|')
plt.legend(loc='best', title='Passband and Stopband', labels=['Epsilon = 0.337', 'Epsilon = 0.45', 'Epsilon = 0.55', 'Epsilon = 0.61', 'Passband', 'Stopband'])
plt.grid(True)
plt.savefig("plot1.png")

