import matplotlib.pyplot as plt

# Read values from values.dat
with open('values.dat', 'r') as file:
    values = [int(line.strip()) for line in file]

# Plot graph
plt.stem(range(-4, 11), values, markerfmt='o', linefmt='-')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid(True)
plt.show()

