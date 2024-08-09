## How to run:
### To enable C++17, use the following command:
    g++ -std=c++17 ./QAM/qam_modem.cpp -o qam_modem
#### To run the program, use this command:
    ./qam_modem

### python plot qpsk constellation
python3 ./QAM/qam_constellation.py

### python modulate qpsk
python3 ./QAM/modulate_qam.py

# Theory
Quadrature Amplitude Modulation (QAM) is a modulation scheme used in digital communications that combines two amplitude-modulated signals into a single channel, effectively increasing the efficiency of data transmission. Here are the key aspects of QAM:

1. **Combination of Amplitude and Phase Modulation**:
   - QAM uses both amplitude and phase modulation to represent data. This is achieved by combining two carrier waves that are out of phase with each other by 90 degrees (hence the term "quadrature").
   - One carrier wave is called the in-phase component (I) and the other is called the quadrature component (Q).

2. **Constellation Diagram**:
   - QAM is often visualized using a constellation diagram where each point represents a unique combination of amplitude and phase.
   - The position of each point on the diagram indicates the specific amplitude and phase of the signal.
   - The number of points on the constellation diagram corresponds to the number of different symbols that can be transmitted. For example, 16-QAM has 16 points, 64-QAM has 64 points, etc.

3. **Higher Data Rates**:
   - By increasing the number of points in the constellation diagram, QAM can transmit more bits per symbol. For example, 16-QAM can transmit 4 bits per symbol (since \(2^4 = 16\)), and 64-QAM can transmit 6 bits per symbol (since \(2^6 = 64\)).
   - Higher-order QAM schemes (like 256-QAM) allow for even higher data rates but require better signal quality to distinguish between closely spaced points.

4. **Efficiency**:
   - QAM is more bandwidth-efficient compared to other modulation schemes such as ASK (Amplitude Shift Keying) or PSK (Phase Shift Keying) because it transmits more bits per symbol.
   - This efficiency makes QAM suitable for applications requiring high data rates, such as digital television, cable modem, and cellular networks.

5. **Noise and Distortion Sensitivity**:
   - One drawback of QAM is its sensitivity to noise and distortion. As the number of points in the constellation increases, the points become closer together, making it harder to distinguish between them in the presence of noise.
   - High-order QAM schemes require a higher Signal-to-Noise Ratio (SNR) for accurate demodulation.

In summary, QAM is a powerful modulation technique used in digital communications that allows for high data rates by combining amplitude and phase modulation. Its effectiveness depends on the balance between achieving higher data rates and maintaining signal integrity in the presence of noise.

## Code Explanation:

### QAM Constellation Generation:
The generateQAMConstellation function creates the constellation points for 16-QAM.

### Modulation:
The modulate function maps the input bits to the QAM symbols using the generated constellation points.

### Demodulation:
The demodulate function retrieves the original bits from the received QAM symbols by finding the closest constellation point.

## QAM theoretical introduction

Quadrature Amplitude Modulation (QAM) is a modulation scheme that conveys data by changing the amplitude of two carrier waves, generally sinusoids, which are out of phase by 90 degrees (hence "quadrature"). QAM is utilized in both analog and digital radio communications and is particularly prominent in digital television and cable networking technologies. Here’s a simplified theoretical introduction to QAM:

### 1. Concept of QAM:
QAM combines both amplitude modulation (AM) and phase modulation (PM) to increase the efficiency of data transmission. It is capable of conveying multiple bits per symbol, thereby enabling higher data rates over a given bandwidth compared to simpler modulation schemes like Amplitude Modulation (AM) or Phase Modulation (PM).

### 2. Key Components:
- **I (In-phase) and Q (Quadrature) Channels**: QAM sends two signals simultaneously using the same frequency but 90 degrees out of phase. One signal modulates the in-phase component (I), and the other modulates the quadrature-phase component (Q). By varying both the amplitude and the phase of these two signals, QAM encodes more information than other simpler types.
- **Constellation Diagram**: This is a representation of the positions of the possible symbols in QAM. It shows the amplitude and phase of the symbols where each point represents a unique symbol.

### 3. Types of QAM:
QAM can be categorized by the number of possible distinct signals (or "constellation points") it can transmit. Common types include 16-QAM, 64-QAM, and 256-QAM. The number typically represents the total number of different combinations of amplitude and phase that can be used, with each symbol representing multiple bits:
- **16-QAM**: Each symbol represents 4 bits.
- **64-QAM**: Each symbol represents 6 bits.
- **256-QAM**: Each symbol represents 8 bits.

### 4. Benefits of QAM:
- **Efficiency**: QAM is more bandwidth-efficient, transmitting more data over the same channel than simpler methods.
- **Flexibility**: The variety of QAM formats allows for flexibility in balancing the trade-offs between data rate and noise susceptibility.

### 5. Challenges:
- **Noise Sensitivity**: Higher-order QAM (like 256-QAM) is more susceptible to noise because the symbols are closer together in the constellation diagram, making it harder to distinguish between them when noise is present.
- **Nonlinear Distortion**: QAM is also sensitive to nonlinear distortion, which can cause the points in the constellation diagram to merge, leading to errors in the received data.

### 6. Applications:
QAM is widely used in cable television systems (to carry TV, internet, and voice signals over the same medium), digital telephony, and some wireless and fiber optic communication systems. The ability of QAM to efficiently transmit large amounts of data makes it ideal for today's high-speed communication requirements.

QAM's ability to combine phase and amplitude modulation to maximize the efficiency of the transmission medium has made it fundamental in both terrestrial and satellite communications networks.
