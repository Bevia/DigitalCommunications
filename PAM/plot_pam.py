import numpy as np
import matplotlib.pyplot as plt
import random

# Function to generate random binary data (0 or 1)
def generate_random_data(length):
    return [random.randint(0, 1) for _ in range(length)]

# Function to perform Pulse Amplitude Modulation (PAM)
def pam_modulation(data, M):
    modulated_signal = []
    
    # 2-PAM maps {0 -> -1, 1 -> +1}, for example
    # Higher order PAM maps symbols to different amplitude levels
    for bit in data:
        # For binary PAM (M=2), map 0 -> -1 and 1 -> +1
        if M == 2:
            modulated_signal.append(2*bit - 1)  # Maps 0 to -1, 1 to +1
        else:
            # For higher-order PAM, map based on PAM levels
            # Map bits to a symbol using Gray coding or standard mapping
            # Example for 4-PAM: 0 -> -3, 1 -> -1, 2 -> 1, 3 -> 3
            raise NotImplementedError("Only binary (2-PAM) is currently implemented.")
    
    return np.array(modulated_signal)

# Plot the PAM signal
def plot_pam_signal(signal, title):
    plt.figure(figsize=(10, 4))
    plt.stem(signal, use_line_collection=True)
    plt.title(title)
    plt.xlabel('Symbol Index')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.show()

# Parameters
data_length = 20  # Length of the binary data sequence
M = 2  # PAM order (M=2 for Binary PAM, M=4 for 4-PAM, etc.)

# Generate random binary data
data = generate_random_data(data_length)

# Perform PAM modulation
pam_signal = pam_modulation(data, M)

# Plot the PAM-modulated signal
plot_pam_signal(pam_signal, title=f'{M}-PAM Modulated Signal')
