import numpy as np
import matplotlib.pyplot as plt

def generate_qam_constellation(M):
    m_sqrt = int(np.sqrt(M))
    constellation = []
    for i in range(m_sqrt):
        for j in range(m_sqrt):
            constellation.append((2 * i - m_sqrt + 1) + 1j * (2 * j - m_sqrt + 1))
    return np.array(constellation)

def modulate(bits, constellation):
    k = int(np.log2(len(constellation)))
    symbols = []
    for i in range(0, len(bits), k):
        index = 0
        for j in range(k):
            index = (index << 1) | bits[i + j]
        symbols.append(constellation[index])
    return np.array(symbols)

def add_noise(symbols, snr_db):
    snr_linear = 10**(snr_db / 10)
    power_symbol = np.mean(np.abs(symbols)**2)
    noise_power = power_symbol / snr_linear
    noise = np.sqrt(noise_power / 2) * (np.random.randn(len(symbols)) + 1j * np.random.randn(len(symbols)))
    return symbols + noise

def plot_constellation(symbols, title):
    plt.figure(figsize=(8, 8))
    plt.scatter(symbols.real, symbols.imag, color='blue', marker='.')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.title(title)
    plt.xlabel('In-phase')
    plt.ylabel('Quadrature')
    plt.show()

def main():
    # Parameters
    M = 16  # 16-QAM
    num_bits = 1000  # Number of bits to transmit
    snr_db = 20  # Signal-to-noise ratio in dB

    # Generate 16-QAM constellation
    constellation = generate_qam_constellation(M)

    # Generate random bits
    bits = np.random.randint(0, 2, num_bits)
    
    # Ensure the length of bits is a multiple of log2(M)
    k = int(np.log2(M))
    if len(bits) % k != 0:
        bits = np.append(bits, np.zeros(k - (len(bits) % k)))

    # Modulate the bits
    symbols = modulate(bits, constellation)

    # Plot constellation without noise
    plot_constellation(symbols, '16-QAM Constellation (No Noise)')

    # Add noise to the symbols
    noisy_symbols = add_noise(symbols, snr_db)

    # Plot constellation with noise
    plot_constellation(noisy_symbols, f'16-QAM Constellation (SNR = {snr_db} dB)')

if __name__ == "__main__":
    main()
