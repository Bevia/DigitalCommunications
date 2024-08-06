import numpy as np
import matplotlib.pyplot as plt
import random

def generate_random_data(num_bits):
    return [random.randint(0, 1) for _ in range(num_bits)]

def qpsk_modulation(data):
    modulated_data = []
    for i in range(0, len(data), 2):
        real = 1 if data[i] == 0 else -1
        imag = 1 if data[i+1] == 0 else -1
        modulated_data.append(complex(real, imag))
    return np.array(modulated_data)

def plot_constellation(modulated_data):
    plt.figure(figsize=(6, 6))
    plt.scatter(modulated_data.real, modulated_data.imag, color='blue')
    plt.title('QPSK Constellation Diagram')
    plt.xlabel('In-Phase')
    plt.ylabel('Quadrature')
    plt.grid(True)
    plt.axhline(0, color='black', lw=0.5)
    plt.axvline(0, color='black', lw=0.5)
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.show()

# Parameters
num_bits = 100  # Number of bits to generate

# Generate random data
data = generate_random_data(num_bits)

# Perform QPSK modulation
modulated_data = qpsk_modulation(data)

# Plot the constellation diagram
plot_constellation(modulated_data)
