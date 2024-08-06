import numpy as np
import matplotlib.pyplot as plt
import random
import scipy.fftpack

# Generate random data bits
def generate_random_data(num_bits):
    return [random.randint(0, 1) for _ in range(num_bits)]

# QPSK modulation
def qpsk_modulation(data):
    modulated_data = []
    for i in range(0, len(data), 2):
        real = 1 if data[i] == 0 else -1
        imag = 1 if data[i+1] == 0 else -1
        modulated_data.append(complex(real, imag))
    return np.array(modulated_data)

# Perform IFFT
def perform_ifft(data):
    return scipy.fftpack.ifft(data)

# Add cyclic prefix
def add_cyclic_prefix(data, cp_len):
    cp_data = np.concatenate([data[-cp_len:], data])
    return cp_data

# Plot the constellation diagram
def plot_constellation(modulated_data, title='Constellation Diagram'):
    plt.figure(figsize=(6, 6))
    plt.scatter(modulated_data.real, modulated_data.imag, color='blue')
    plt.title(title)
    plt.xlabel('In-Phase')
    plt.ylabel('Quadrature')
    plt.grid(True)
    plt.axhline(0, color='black', lw=0.5)
    plt.axvline(0, color='black', lw=0.5)
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.show()

# Plot the time domain signal
def plot_time_domain_signal(signal, title='Time Domain Signal'):
    plt.figure(figsize=(10, 4))
    plt.plot(np.real(signal), label='Real part')
    plt.plot(np.imag(signal), label='Imaginary part')
    plt.title(title)
    plt.xlabel('Sample index')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.legend()
    plt.show()

# Parameters
num_subcarriers = 64
cp_len = 16
num_bits = num_subcarriers * 2  # Number of bits to generate (QPSK uses 2 bits per symbol)

# Generate random data
data = generate_random_data(num_bits)

# Perform QPSK modulation
modulated_data = qpsk_modulation(data)

# Map QPSK symbols to OFDM subcarriers
ofdm_data = np.zeros(num_subcarriers, dtype=complex)
ofdm_data[:len(modulated_data)] = modulated_data

# Perform IFFT to convert to time domain
ifft_data = perform_ifft(ofdm_data)

# Add cyclic prefix
tx_signal = add_cyclic_prefix(ifft_data, cp_len)

# Plot the constellation diagram of the modulated data
plot_constellation(modulated_data, title='QPSK Constellation Diagram')

# Plot the time domain signal with cyclic prefix
plot_time_domain_signal(tx_signal, title='OFDM Time Domain Signal with Cyclic Prefix')

# To observe the effect of OFDM, we can remove the cyclic prefix and plot the constellation diagram
rx_signal = tx_signal[cp_len:]  # Remove cyclic prefix
rx_fft_data = scipy.fftpack.fft(rx_signal)  # Perform FFT to go back to frequency domain

# Plot the constellation diagram of the received data
plot_constellation(rx_fft_data, title='Received Constellation Diagram After OFDM')
