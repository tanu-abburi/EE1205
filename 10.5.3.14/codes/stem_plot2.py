import numpy as np
import matplotlib.pyplot as plt

# Define the values
n_values = np.arange(0, 25)
y_values = np.zeros(25)
x_values = np.zeros(25)

# Calculate y(n) using the given difference equation
for n in range(1, 25):
    y_values[n] = y_values[n-1] + (2*n + 1)

# Calculate x(n) using the difference equation x(n) = y(n) - y(n-1)
for n in range(1, 25):
    x_values[n] = y_values[n] - y_values[n-1]

# Plot the stimulated result and the analysis result
plt.plot(n_values, x_values, label='Stimulated Result')
plt.plot(24, 625, 'ro', label='Analysis Result (n=24)')
plt.xlabel('n')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()

