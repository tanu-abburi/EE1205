import numpy as np
import matplotlib.pyplot as plt

def x_n(n):
    return (5 + 3 * n) * (n >= 0)

# Generate values for n from 0 to 10
n_values = np.arange(0, 11, 1)

# Calculate corresponding x(n) values
x_values = [x_n(n) for n in n_values]

# Create a stem plot
plt.stem(n_values, x_values, basefmt='b-', linefmt='b-', markerfmt='bo')

# Set plot labels and title
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('Stem Plot of x(n) = (5 + 3n)u(n)')

# Display the plot
plt.show()

