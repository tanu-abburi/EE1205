import numpy as np
import matplotlib.pyplot as plt

# Define the sequence function x_n = (5+3n)u(n)
def x_n(n):
    return (5 + 3 * n) * (n >= 0)

# Generate values of n from -10 to 10
n_values = np.arange(-5, 11)

# Calculate corresponding x_n values
x_values = np.array([x_n(n) for n in n_values])

# Create a stem plot
plt.stem(n_values, x_values)
plt.xlabel('n')
plt.ylabel('x_n')
plt.title('Stem Plot of x_n = (5+3n)u(n)')
plt.grid(True)
plt.show()

