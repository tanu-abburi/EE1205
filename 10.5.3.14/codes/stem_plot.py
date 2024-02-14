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
plt.stem(x_values, y_values, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.xlabel('n')
plt.ylabel('y(n)')
plt.grid(True)

# Highlight the point where n=24 with a different color
highlight_index = x_values.index(24)
plt.stem(x_values[highlight_index], y_values[highlight_index], linefmt='r-', markerfmt='ro', basefmt='r-')

# Add (n, y(n)) text above the plot, slightly to the left
plt.text(x_values[highlight_index] - 1.2, y_values[highlight_index] + 29, f'({x_values[highlight_index]}, {y_values[highlight_index]})', ha='center')

plt.show()

