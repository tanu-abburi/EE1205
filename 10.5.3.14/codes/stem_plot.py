import numpy as np
import matplotlib.pyplot as plt

# Function to calculate y(n)
def y(n):
    return (n**2 + 2*n + 1) if n >= 0 else 0

# Read values of x(n) from values.dat
with open('values.dat', 'r') as file:
    x_values = [int(line.strip()) for line in file]

# Calculate y(n) for each x(n)
y_values = [y(n) for n in x_values]

# Plot the graph
plt.stem(x_values, y_values)
plt.xlabel('n')
plt.ylabel('y(n)')
plt.grid(True)
plt.show()

