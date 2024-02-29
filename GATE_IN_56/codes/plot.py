import numpy as np
import matplotlib.pyplot as plt

# Function to calculate y (voltage gain) for a given f (frequency)
def calculate_y(f):
    return 20 - 10 * np.log10((f**2 * 10**-8 * 4 * np.pi**2) + 1)

# Generate values for f from 0 Hz to 20 kHz
f_values = np.linspace(0, 20e3, 1000)

# Calculate corresponding y values
y_values = calculate_y(f_values)

# Find the index where y_values crosses zero
zero_index = np.where(np.diff(np.sign(y_values)))[0][0]

# Get the corresponding frequency value where y is zero
f_at_y_0 = f_values[zero_index]

# Plot
plt.plot(f_values, y_values)
plt.plot(f_at_y_0, 0, 'ro', label=f'f at y=0: {f_at_y_0:.2f} Hz')  # Highlight the point where y is zero
plt.xlabel('Frequency (Hz)')
plt.ylabel('Voltage Gain (dB)')
plt.grid(True)
plt.legend()
plt.show()

