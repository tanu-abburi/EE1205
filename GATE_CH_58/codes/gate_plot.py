import numpy as np
import matplotlib.pyplot as plt

# Read data from values.dat
data = np.loadtxt('values.dat')

# Extract t and a(t) values
t = data[:, 0]
a_t = data[:, 1]

# Plot a(t) vs t
plt.plot(t, a_t)
plt.xlabel('t')
plt.ylabel('a(t)')
plt.grid(True)

# Highlight value of a(t) at t=10
t_highlight = 10
a_t_highlight = a_t[np.where(t == t_highlight)][0]
plt.scatter(t_highlight, a_t_highlight, color='red', label=f'a({t_highlight}) = {a_t_highlight}')
plt.legend()

# Show plot
plt.show()

