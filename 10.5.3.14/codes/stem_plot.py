import numpy as np
import matplotlib.pyplot as plt

# Load data from values.dat
y_values = np.loadtxt('values.dat')

# Generate values of n from 0 to 26
n = np.arange(0, 27)

# Create a new figure
plt.figure(figsize=(10, 5))

# Plot y(n) using scatter plot with larger markers
plt.plot(n, y_values, 'ro', markersize=10, label='Scatter Plot of y(n)')

# Highlight point where n=24 with a different color
highlight_index = 24
plt.plot(n[highlight_index], y_values[highlight_index], 'go', markersize=12, label='n=24', zorder=3)

# Plot y(n) using stem plot
plt.stem(n, y_values, linefmt='b-', markerfmt='bo', basefmt=' ', label='Stem Plot of y(n)')

plt.xlabel('n')
plt.ylabel('y(n)')
plt.legend()
plt.grid(True)

plt.show()

