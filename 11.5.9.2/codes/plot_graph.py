import numpy as np
import matplotlib.pyplot as plt

# Load data from file
data = np.loadtxt('values.dat')

# Generate values of n
n = np.arange(-4, 11)

# Plot graph
plt.stem(n, data)
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('Plot of x(n) = (1 + 2n)u(n)')
plt.grid(True)
plt.show()

