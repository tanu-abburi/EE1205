import matplotlib.pyplot as plt

# Read values from the text file
with open("values.txt", "r") as file:
    values = [int(line.strip()) for line in file]

# Generate x values (assuming n starts from 1)
n_values = list(range(1, len(values) + 1))

# Plot stem graph
plt.stem(n_values, values, use_line_collection=True)
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('Stem Graph of x(n) = 5 + 3n')
plt.savefig('tan_plot.png', dpi = 300, bbox_inches = 'tight')

