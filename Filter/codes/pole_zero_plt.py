import numpy as np
import matplotlib.pyplot as plt

# Read pole data from the txt file
data = np.loadtxt('poles.txt', delimiter=',', skiprows=1)

# Separate real and imaginary parts
real_parts = data[:, 0]
imaginary_parts = data[:, 1]

# Identify poles on the left side of the complex plane
left_poles_indices = real_parts < 0
left_real_parts = real_parts[left_poles_indices]
left_imaginary_parts = imaginary_parts[left_poles_indices]

# Plot poles
plt.scatter(real_parts[~left_poles_indices], imaginary_parts[~left_poles_indices], c='r', marker='x', label='Poles (Right)')
plt.scatter(left_real_parts, left_imaginary_parts, c='b', marker='x', label='Poles (Left)')

# Add labels and title
plt.xlabel('Real Part')
plt.ylabel('Imaginary Part')
plt.title('Pole-Zero Plot')

# Set aspect ratio to equal
plt.axis('equal')

# Draw real and imaginary axes
plt.axhline(0, color='k', linestyle='--', linewidth=1)  # Vertical line for the imaginary axis
plt.axvline(0, color='g', linestyle='--', linewidth=1)  # Horizontal line for the real axis

# Add legend
plt.legend(loc='upper left')

# Display the plot
plt.grid(True)
plt.savefig("Pole_Zero_plt.png")
