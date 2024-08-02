import numpy as np
import matplotlib.pyplot as plt

# Define the QPSK symbols using complex numbers
QPSK_SYMBOLS = {
    (0, 0): 1 + 1j,
    (0, 1): -1 + 1j,
    (1, 1): -1 - 1j,
    (1, 0): 1 - 1j
}

def bits_to_qpsk(bitstream):
    """ Convert a bitstream to QPSK symbols. """
    symbols = []
    for i in range(0, len(bitstream), 2):
        bit_pair = (bitstream[i], bitstream[i+1])
        symbols.append(QPSK_SYMBOLS[bit_pair])
    return np.array(symbols)

def add_noise(symbols, noise_level=0.1):
    """ Add Gaussian noise to the QPSK symbols. """
    noise = noise_level * (np.random.randn(len(symbols)) + 1j * np.random.randn(len(symbols)))
    return symbols + noise

# Example bit stream to be transmitted
bit_stream = [0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0]

# Modulate the bit stream using QPSK
modulated_signal = bits_to_qpsk(bit_stream)

# Add noise to the signal
noisy_signal = add_noise(modulated_signal, noise_level=0.3)

# Plot the constellation diagram
plt.figure(figsize=(8, 8))
plt.scatter(noisy_signal.real, noisy_signal.imag, color='red', label='Noisy Signal')
plt.scatter(modulated_signal.real, modulated_signal.imag, color='blue', label='Original Signal', alpha=0.5)
plt.axhline(y=0, color='k', linestyle='--', linewidth=0.5)
plt.axvline(x=0, color='k', linestyle='--', linewidth=0.5)
plt.grid(True)
plt.title('QPSK Constellation Diagram')
plt.xlabel('In-Phase')
plt.ylabel('Quadrature')
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.legend()
plt.show()
