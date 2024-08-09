In telecommunications, several modulation schemes are commonly used beyond Quadrature Phase Shift Keying (QPSK), Binary Phase Shift Keying (BPSK), and Quadrature Amplitude Modulation (QAM). Some of the main modulation schemes include:

1. **Frequency Shift Keying (FSK)**:
   - **Description**: FSK modulates the frequency of the carrier signal to represent data. The simplest form, Binary FSK (BFSK), uses two frequencies to represent binary 0 and 1.
   - **Applications**: Used in radio transmissions, RFID systems, and early modems.

2. **Amplitude Shift Keying (ASK)**:
   - **Description**: ASK modulates the amplitude of the carrier signal to represent data. Binary ASK (BASK) uses two different amplitudes to represent binary 0 and 1.
   - **Applications**: Used in optical fiber communications and RFID systems.

3. **Phase Shift Keying (PSK)**:
   - **Beyond BPSK and QPSK**:
     - **8-PSK (8-Phase Shift Keying)**: Uses eight different phase shifts to encode three bits per symbol.
     - **16-PSK**: Uses sixteen phase shifts to encode four bits per symbol.

4. **Orthogonal Frequency Division Multiplexing (OFDM)**:
   - **Description**: OFDM divides the data stream into several parallel sub-streams, each modulated by a different carrier frequency. These sub-carriers are orthogonal to each other, minimizing interference.
   - **Applications**: Widely used in modern broadband communications, including Wi-Fi, LTE, and digital television.

5. **Spread Spectrum Techniques**:
   - **Direct Sequence Spread Spectrum (DSSS)**: Data is spread over a wide frequency band by multiplying the signal with a pseudo-random noise code.
   - **Frequency Hopping Spread Spectrum (FHSS)**: The carrier frequency hops among many frequencies according to a pseudo-random sequence.
   - **Applications**: Used in military communications, GPS, and some wireless LAN technologies (e.g., early versions of Wi-Fi).

6. **Pulse Amplitude Modulation (PAM)**:
   - **Description**: PAM modulates the amplitude of pulses in a signal. Each pulse can have multiple amplitude levels to encode more than one bit per pulse.
   - **Applications**: Used in Ethernet and some optical fiber communication systems.

7. **Trellis Coded Modulation (TCM)**:
   - **Description**: TCM combines modulation and error correction coding in one process, using a trellis diagram to improve data reliability without increasing bandwidth.
   - **Applications**: Used in high-speed modem standards, such as V.32 and V.34.

8. **Carrierless Amplitude Phase (CAP)**:
   - **Description**: CAP modulation is similar to QAM but does not require a carrier signal, making it more efficient for certain applications.
   - **Applications**: Used in some DSL technologies.

These modulation schemes are chosen based on various factors like bandwidth efficiency, power efficiency, noise immunity, and implementation complexity. They play a crucial role in determining the performance and reliability of telecommunications systems.