## How to run:
### To enable C++17, use the following command:
    g++ -std=c++17 ./QAM/qam_modem.cpp -o qam_modem
#### To run the program, use this command:
    ./qam_modem

### python plot qpsk constellation
python3 ./QPSK/qam_constellation.py

### python modulate qpsk
python3 ./QPSK/modulate_qpsk.py

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