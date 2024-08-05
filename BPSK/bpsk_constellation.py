import numpy as np
import matplotlib.pyplot as plt

# Generate BPSK modulated signal points
def bpsk_modulate(data):
    return np.array([1 if bit == 0 else -1 for bit in data])

# Generate random binary data
np.random.seed(0)
data_length = 100
data = np.random.randint(0, 2, data_length)

# BPSK modulation
bpsk_signal = bpsk_modulate(data)

# Plot the constellation diagram
plt.figure(figsize=(8, 8))
plt.scatter(bpsk_signal, np.zeros_like(bpsk_signal), color='red', marker='x', label='Ideal Signal')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.title('BPSK Constellation Diagram (Without Noise)')
plt.xlabel('In-phase')
plt.ylabel('Quadrature')
plt.legend()
plt.show()
