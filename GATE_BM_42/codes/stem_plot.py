import numpy as np
import matplotlib.pyplot as plt

# Load values from the file
values = np.loadtxt('values.dat')

# Generate corresponding time values
t_values = np.arange(0, len(values) / 10, 0.1) # Adjust the step size as needed

# Plot the values
plt.plot(t_values, values)

# Highlight the value at t = 0
plt.scatter(0, values[0], color='red', label='t=0')

plt.xlabel('t')
plt.ylabel('g(t)')
plt.legend()
plt.grid(True)
plt.show()

