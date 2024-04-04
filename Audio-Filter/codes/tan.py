import soundfile as sf
from scipy import signal

# Read .wav file 
input_signal, fs = sf.read('tanusha.wav') 

# Sampling frequency of Input signal
sampl_freq = fs

# Order of the filter
order = 4   

# Cutoff frequency 1kHz
cutoff_freq = 1000.0  

# Digital frequency
Wn = 2 * cutoff_freq / sampl_freq  

# Generate the Butterworth filter coefficients
b, a = signal.butter(order, Wn, 'low') 

# Print the coefficients
print("a coefficients:", a)
print("b coefficients:", b)

# Filter the input signal with Butterworth filter
output_signal = signal.lfilter(b, a, input_signal)

# Write the output signal into .wav file
sf.write('filtered.wav', output_signal, fs)

