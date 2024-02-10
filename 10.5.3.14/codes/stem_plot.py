import numpy as np
import matplotlib.pyplot as plt

def x(n):
    return (1 + 2 * n) * (n >= 0)

# Generate values of n from -10 to 10
n_values = np.arange(-5, 8)

# Calculate corresponding values of x(n)
x_values = x(n_values)

# Plot the graph
plt.stem(n_values, x_values)
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('Graph of x(n) = (1 + 2n)u(n)')
plt.grid(True)
plt.show()

