import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Define the cutoff frequency
wc = 0.025 * np.pi

# Create a frequency vector
w = np.linspace(-np.pi, np.pi, 1000)

# Define the magnitude response
magnitude_response = np.zeros_like(w)
magnitude_response[np.abs(w) <= wc] = 1

# Compute the phase response (it's zero for simplicity)
phase_response = np.zeros_like(w)


h = magnitude_response * np.exp(1j * phase_response)

# Plot the frequency response
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(w, np.abs(h), 'b')
plt.scatter(wc,0, color='r' , label='cut-off frequency') 

plt.title('Low Pass Filter Frequency Response')
plt.xlabel(r'$\omega$')
plt.ylabel('Magnitude')
plt.legend()
plt.grid()


n = np.arange(-50, 51)
impulse_response = np.zeros_like(n, dtype=float)
for i, ni in enumerate(n):
    if ni == 0:
        impulse_response[i] = wc / np.pi
    else:
        impulse_response[i] = np.sin(wc * ni) / (ni * np.pi)

# Plot the impulse response
plt.subplot(2, 1, 2)
plt.stem(n, impulse_response)
#plt.xlim(-10, 10)
plt.title('Impulse Response')
plt.xlabel('n')
plt.ylabel('h(n)')
plt.grid()
plt.savefig("LPF_FIR.png")




