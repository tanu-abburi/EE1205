import numpy as np
import matplotlib.pyplot as plt

# Define the piecewise function h_LP(n)


# Generate values for n
n_values = np.arange(-480, 491)
h_Lp = np.where((n_values != 0) & (n_values >= -100) & (n_values <= 100), np.sin(n_values * np.pi / 40) / (n_values * np.pi), 0)



# Calculate the DTFT using numpy's FFT
H_freq_response = np.fft.fftshift(np.fft.fft(h_Lp))

# Angular frequency axis (normalized)
omega_normalized = np.linspace(-np.pi/2, np.pi/2, len(n_values))

# Plotting
plt.plot(omega_normalized/np.pi, np.abs(H_freq_response))
plt.xlabel('($\omega$/pi)')
plt.ylabel('|H(r$\omega$)|')
plt.title('FIR LOW PASS FILTER')
plt.grid(True)

plt.savefig("FIR_Low_Filter.png")
