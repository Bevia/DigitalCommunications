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
        despread_bit = np