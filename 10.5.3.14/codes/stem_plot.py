import matplotlib.pyplot as plt

# Function to read data from file
def read_data(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            data.append(int(line.strip()))
    return data

# Read data from files
theory_data = read_data('theory.dat')
simulated_data = read_data('simulated.dat')

# Plotting
plt.plot(range(len(theory_data)), theory_data, marker='o', label='Theory')
plt.plot(range(len(simulated_data)), simulated_data, marker='^', label='Simulated')
plt.xlabel('Index')
plt.ylabel('Value')

# Highlighting the point (24, 625)
plt.scatter([24], [625], color='green', label='(24, 625)', s=100)  # Increase size (s) of the marker

plt.legend()
plt.show()

