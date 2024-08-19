import numpy as np
import matplotlib.pyplot as plt
import random

# Function to generate random binary data (0 or 1)
def generate_random_data(length):
    return [random.randint(0, 1) for _ in range(length)]

# Function to generate a PN sequence (spreading code)
def generate_pn_sequence(length):
    return [random.choice([-1, 1]) for _ in range(length)]

# Function to spread the data using DSSS
def spread_data(data, pn_sequence):
    spread_signal = []
    for bit in data:
        spread_bit = [bit * chip for chip in pn_sequence]
        spread_signal.extend(spread_bit)
    return np.array(spread_signal)

# Function to despread the received signal
def despread_data(spread_signal, pn_sequence):
    despread_signal = []
    chips_per_bit = len(pn_sequence)
    for i in range(0, len(spread_signal), chips_per_bit):
        chunk = spread_signal[i:i + chips_per_bit]
        despread_bit = np.sign(np.dot(chunk, pn_sequence))  # Correlate with PN sequence
        despread_signal.append(1 if despread_bit > 0 else 0)
    return np.array(despread_signal)

# Parameters
data_length = 10   # Length of the binary data sequence
pn_length = 8      # Length of the PN sequence (chips per bit)

# Generate random binary data and PN sequence
data = generate_random_data(data_length)
pn_sequence = generate_pn_sequence(pn_length)

# Spread the data using DSSS
spread_signal = spread_data(data, pn_sequence)

# Simulate the received signal (for simplicity, no noise or interference added)
received_signal = spread_signal

# Despread the received signal to recover the original data
despread_data = despread_data(received_signal, pn_sequence)

# Disable interactive mode
plt.ioff()

# Plot the results
fig, axs = plt.subplots(4, 1, figsize=(10, 12))

# Plot the original data
axs[0].stem(data)
axs[0].set_title('Original Data')
axs[0].set_xlabel('Bit Index')
axs[0].set_ylabel('Bit Value')
axs[0].set_ylim(-0.2, 1.2)

# Plot the PN sequence
axs[1].stem(pn_sequence)
axs[1].set_title('PN Sequence')
axs[1].set_xlabel('Chip Index')
axs[1].set_ylabel('Chip Value')

# Plot the spread signal
axs[2].plot(spread_signal)
axs[2].set_title('Spread Signal (DSSS Output)')
axs[2].set_xlabel('Sample Index')
axs[2].set_ylabel('Amplitude')

# Plot the recovered data after despreading
axs[3].stem(despread_data)
axs[3].set_title('Recovered Data After Despreading')
axs[3].set_xlabel('Bit Index')
axs[3].set_ylabel('Bit Value')
axs[3].set_ylim(-0.2, 1.2)

# Show the plots
plt.tight_layout()
plt.show()
