
## How to run:
    g++ ./QPSK/qpsk.cpp ./QPSK/qpsk.cpp -o iir 
### To enable C++11, use the following command:
    g++ -std=c++17 ./QPSK/qpsk.cpp -o ./QPSK/qpsk.cpp -o qpsk 
#### To run the program, use this command:
    ./qpsk


## Introduction
Quadrature Phase Shift Keying (QPSK) is a modulation scheme used in digital communications. It represents digital data by modulating the phase of a carrier signal, allowing the transmission of two bits per symbol. Here's a detailed explanation:

### Key Characteristics of QPSK:

1. **Phase Modulation:**
   - QPSK modulates the phase of a carrier signal to encode data.
   - It uses four distinct phase shifts (0°, 90°, 180°, and 270°), each representing a unique combination of two bits (00, 01, 10, 11).

2. **Symbol Representation:**
   - Each phase shift corresponds to a symbol that represents two bits of binary data.
   - This allows QPSK to transmit twice as much data as Binary Phase Shift Keying (BPSK) for the same bandwidth.

3. **Constellation Diagram:**
   - A constellation diagram for QPSK shows four points (representing the four phases) equally spaced on a circle.
   - Each point corresponds to one of the four possible phase states.

4. **Bandwidth Efficiency:**
   - QPSK is bandwidth efficient because it transmits two bits per symbol, effectively doubling the data rate compared to BPSK for the same bandwidth.

5. **Bit Error Rate (BER):**
   - QPSK has a higher bit error rate compared to BPSK in the presence of noise, but it balances this with higher data rates.

### How QPSK Works:

1. **Mapping Bits to Phases:**
   - Input data is grouped into pairs of bits.
   - Each pair of bits is mapped to one of the four possible phase states.

2. **Modulation Process:**
   - The carrier signal is modulated in accordance with the mapped phase state.
   - The phase of the carrier changes to reflect the binary pair being transmitted.

3. **Transmission:**
   - The modulated signal is transmitted over the communication channel.
   - At the receiver end, the signal is demodulated to retrieve the original binary data.

### Advantages of QPSK:

- **Higher Data Rates:** By encoding two bits per symbol, QPSK achieves higher data rates compared to BPSK.
- **Spectral Efficiency:** QPSK uses the available bandwidth more efficiently.

### Applications of QPSK:

- **Wireless Communications:** Widely used in cellular networks, Wi-Fi, and satellite communications.
- **Digital Television:** Used in digital TV broadcasting standards like DVB-S (Digital Video Broadcasting - Satellite).

### Example:

Consider a binary input stream: 11010010.

- Grouping into pairs: (11), (01), (00), (10).
- Mapping to phases: 
  - 11 → 270°
  - 01 → 90°
  - 00 → 0°
  - 10 → 180°
- The carrier signal is then modulated to these phases sequentially.

QPSK is a crucial modulation technique in modern digital communication systems, balancing complexity, data rate, and robustness.