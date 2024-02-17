import numpy as np
import matplotlib.pyplot as plt

# Read values from file
with open('values.dat', 'r') as file:
    values = [float(line.strip()) for line in file]

# Generate corresponding time values
t_values = np.arange(0, 16)

# Plot the graph
plt.plot(t_values, values)
plt.xlabel('t')
plt.ylabel('a(t)')
plt.grid(True)

# Highlight value of a(t) at t=10
highlight_t = 10
highlight_a = (-0.25 * highlight_t ** 2 + 10 * highlight_t + 10) / 10
plt.scatter(highlight_t, highlight_a, color='red', label=f'a({highlight_t}) = {highlight_a:.2f}')
plt.legend()

plt.show()

