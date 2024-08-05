import numpy as np
import matplotlib.pyplot as plt

# Generate BPSK modulated signal points
def generate_bpsk_constellation(data):
    constellation = []
    for bit in data:
        if bit == 0:
            constellation.append(1)
        else:
            constellation.append(-1)
    return np.array(constellation)

# Generate random binary data
np.random.seed(0)
data_length = 100
data = np.random.randint(0, 2, data_length)

# BPSK modulation
bpsk_signal = generate_bpsk_constellation(data)

# Add noise to the BPSK signal
noise_std_dev = 0.5
noise = np.random.normal(0, noise_std_dev, bpsk_signal.shape)
noisy_signal = bpsk_signal + noise

# Plot the constellation diagram
plt.figure(figsize=(8, 8))
plt.scatter(noisy_signal, np.zeros_like(noisy_signal), color='blue', marker='o')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.title('BPSK Constellation Diagram')
plt.xlabel('In-phase')
plt.ylabel('Quadrature')
plt.show()
