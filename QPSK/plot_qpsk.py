import matplotlib.pyplot as plt
import numpy as np

# Define the QPSK symbols using complex numbers
qpsk_symbols = np.array([
    1 + 1j,  # 00
    -1 + 1j, # 01
    -1 - 1j, # 11
    1 - 1j   # 10
])

# Plot the constellation diagram
plt.figure(figsize=(6, 6))
plt.scatter(qpsk_symbols.real, qpsk_symbols.imag, color='red')

# Annotate the points
annotations = ['00', '01', '11', '10']
for symbol, annotation in zip(qpsk_symbols, annotations):
    plt.annotate(annotation, (symbol.real, symbol.imag), textcoords="offset points", xytext=(0,10), ha='center')

plt.axhline(y=0, color='k', linestyle='--', linewidth=0.5)
plt.axvline(x=0, color='k', linestyle='--', linewidth=0.5)
plt.grid(True)
plt.title('QPSK Constellation Diagram')
plt.xlabel('In-Phase')
plt.ylabel('Quadrature')
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.show()
