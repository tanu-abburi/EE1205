import numpy as np
import matplotlib.pyplot as plt

# Load data from values.dat
y_values = np.loadtxt('values.dat')

# Generate values of n from 0 to 26
n = np.arange(0, 27)

# Create a new figure
plt.figure(figsize=(10, 5))

# Plot y(n) using scatter plot with larger markers for Simulation
plt.plot(n, y_values, 'ro', markersize=10, label='Simulation')

# Highlight point where n=24 with a different color and shape
highlight_index = 24
plt.plot(n[highlight_index], y_values[highlight_index], 'go', markersize=12, label='n=24', zorder=3)

# Annotate the highlighted point with text (24, 625)
plt.text(n[highlight_index], y_values[highlight_index], '(24, 625)', ha='right', va='bottom')

# Plot y(n) using stem plot with triangle marker for Theory
plt.stem(n, y_values, linefmt='b-', markerfmt='^b', basefmt=' ', label='Theory')

plt.xlabel('n')
plt.ylabel('y(n)')
plt.legend()
plt.grid(True)
plt.show()

