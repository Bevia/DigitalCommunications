
## How to run:
### To enable C++17, use the following command:
    g++ -std=c++17 ./BPSK/bpsk_.cpp -o bpsk_
#### To run the program, use this command:
    ./bpsk_

### python plot qpsk constellation
python3 ./BPSK/bpsk_constellation.py

### python modulate qpsk
python3 ./BPSK/modulate_bpsk.py

# Theory
Binary Phase Shift Keying (BPSK) is a type of digital modulation scheme used in digital communications. It is one of the simplest forms of phase modulation and is widely used due to its robustness and simplicity. Here are the key features and concepts of BPSK:

### Key Features of BPSK:

1. **Binary Modulation:**
   - BPSK is a binary modulation scheme, meaning it represents digital data with two distinct phases of a carrier signal.
   - Each phase corresponds to one of the binary digits (0 or 1).

2. **Phase Shifts:**
   - In BPSK, the carrier signal is phase-shifted by 180 degrees to represent the two binary states.
   - For example, a phase shift of 0 degrees might represent a binary '0', and a phase shift of 180 degrees might represent a binary '1'.

3. **Modulation Process:**
   - The process of modulation involves shifting the phase of the carrier signal according to the binary data.
   - Mathematically, this can be represented as:
     \[
     s(t) = \sqrt{2P} \cdot \cos(2\pi f_c t + \theta)
     \]
     Where:
     - \( P \) is the power of the signal
     - \( f_c \) is the carrier frequency
     - \( \theta \) is the phase shift, which is either 0 or \(\pi\) (180 degrees) for BPSK.

4. **Demodulation:**
   - The process of demodulation involves detecting the phase shifts in the received signal to recover the original binary data.
   - This is typically done using a phase-locked loop (PLL) or other phase detection methods.

5. **Advantages:**
   - Simplicity: BPSK is easy to implement and understand.
   - Robustness: It is relatively immune to noise and interference compared to more complex modulation schemes.
   - Bandwidth Efficiency: BPSK uses bandwidth efficiently, making it suitable for various communication systems.

6. **Disadvantages:**
   - BPSK is not as spectrally efficient as higher-order modulation schemes (e.g., QPSK, 16-QAM).
   - It has a lower data rate compared to more complex modulation schemes.

### Applications of BPSK:

- **Satellite Communications:**
  - BPSK is commonly used in satellite communication systems due to its robustness to noise.
  
- **Deep Space Communications:**
  - Used in space probes and other deep space communication systems for reliable data transmission.
  
- **RFID Systems:**
  - Often employed in Radio Frequency Identification (RFID) systems for tag-reader communication.

- **Wireless LANs:**
  - Used in some wireless local area networks (WLANs) and other wireless communication standards.

In summary, BPSK is a fundamental digital modulation technique known for its simplicity and robustness, making it suitable for a wide range of communication applications.

# Code Explanation

### Binary Data Generation:
The generateBinaryData function creates a random binary data sequence.

### BPSK Modulation:
The bpskModulate function maps each binary bit to a phase shift (0 or 180 degrees) and generates a cosine wave for each bit. The modulated signal is represented as a complex vector.

### Add Noise:
The addNoise function adds Gaussian noise to the modulated signal to simulate a real communication channel.

### BPSK Demodulation:
The bpskDemodulate function correlates the received signal with a reference cosine wave to determine the original binary data.

### Main Function:
The main function ties everything together: it generates binary data, modulates it, adds noise, demodulates the received signal, and prints the results.

This example demonstrates the basic concepts of BPSK modulation and demodulation in a straightforward manner using modern C++.