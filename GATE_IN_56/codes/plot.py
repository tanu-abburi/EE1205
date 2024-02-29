import numpy as np
import matplotlib.pyplot as plt

# Load data from file
data = np.loadtxt('values.dat')

# Extract frequency (f) and voltage gain (y)
frequencies = data[:, 0]
voltage_gain = data[:, 1]

# Plot
plt.figure(figsize=(8, 6))
plt.plot(voltage_gain, frequencies, linestyle='-', color='blue')
plt.title('Frequency vs. Voltage Gain')
plt.xlabel('Voltage Gain (y)')
plt.ylabel('Frequency (f)')
plt.grid(True)

# Highlight the value of f at y=0
f_at_y_0 = frequencies[np.where(voltage_gain == 0)]
plt.scatter(0, f_at_y_0, color='red', label='f at y=0')
plt.legend()
plt.show()

