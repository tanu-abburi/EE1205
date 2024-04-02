import soundfile as sf
from scipy import signal, fft
import numpy as np
from numpy.polynomial import Polynomial as P
from matplotlib import pyplot as plt

def myfiltfilt(b, a, input_signal):
    X = fft.fft(input_signal)
    w = np.linspace(0, 1, len(X) + 1)
    W = np.exp(2j*np.pi*w[:-1])
    B = np.abs(np.polyval(b, W)) ** 2
    A = np.abs(np.polyval(a, W)) ** 2
    # Ensure B and A have compatible shapes for element-wise multiplication
    B = np.reshape(B, (-1, 1))
    A = np.reshape(A, (-1, 1))
    Y = B*(1/A)*X
    return fft.ifft(Y).real

# Read .wav file 
input_signal, fs = sf.read('vinay.wav') 
print(len(input_signal))
np.savetxt("in.txt", input_signal)

# Sampling frequency of Input signal
sampl_freq = fs

# Order of the filter
order = 4   

# Cutoff frequency 4kHz
cutoff_freq = 5000.0  

# Digital frequency
Wn = 2 * cutoff_freq / sampl_freq  

# b and a are numerator and denominator polynomials respectively
b, a = signal.butter(order, Wn, 'low') 

# Filter the input signal with butterworth filter
output_signal = signal.filtfilt(b, a, input_signal, padlen=1)

op1 = myfiltfilt(b, a, input_signal)
x_plt = np.arange(len(input_signal))
plt.plot(x_plt[1000:10000], output_signal[1000:10000], 'orange', label='Output by built-in function')
plt.plot(x_plt[1000:10000], output_signal[1000:10000], 'green',label='Output by not using built-in function')
plt.title("Verification of outputs of Audio Filter")
plt.grid()
plt.legend()
plt.savefig("Audio_Filter_verf.png")

