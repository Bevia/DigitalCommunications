import numpy as np
import matplotlib.pyplot as plt

def generate_qam_constellation(M):
    m_sqrt = int(np.sqrt(M))
    constellation = []
    for i in range(m_sqrt):
        for j in range(m_sqrt):
            constellation.append((2 * i - m_sqrt + 1) + 1j * (2 * j - m_sqrt + 1))
    return np.array(constellation)

def plot_constellation(constellation, M):
    plt.figure(figsize=(8, 8))
    plt.scatter(constellation.real, constellation.imag, color='blue')
    for point in constellation:
        plt.text(point.real, point.imag, f'({point.real:.1f}, {point.imag:.1f})', fontsize=12, ha='right')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.title(f'{M}-QAM Constellation Diagram')
    plt.xlabel('In-phase')
    plt.ylabel('Quadrature')
    plt.show()

# Parameters
M = 16  # 16-QAM

# Generate and plot the constellation diagram
constellation = generate_qam_constellation(M)
plot_constellation(constellation, M)
