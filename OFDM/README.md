
## How to run:
    g++ ./OFDM/ofdm_.cpp ./OFDM/ofdm_.cpp -o ofdm 
### To enable C++11, use the following command:
    g++ -std=c++11 ./OFDM/ofdm_.cpp -o ./OFDM/ofdm_.cpp -o ofdm 
#### To run the program, use this command:
    ./ofdm

### compile the FTTW3 library...find the route of the lib and do the following:
g++ -std=c++11 -o ofdm_ ./OFDM/ofdm_.cpp -lfftw3 -L/opt/homebrew/Cellar/fftw/3.3.10_1/lib/ -I/opt/homebrew/Cellar/fftw/3.3.10_1/include

## OFDM Theory
This example focuses on the basic steps of OFDM: generating random data, performing the Inverse Fast Fourier Transform (IFFT) to create OFDM symbols, and adding a cyclic prefix for transmission. This example uses the FFTW library for performing the IFFT.

### Orthogonal Frequency Division Multiplexing (OFDM):

Description: OFDM divides the data stream into several parallel sub-streams, each modulated by a different carrier frequency. 
These sub-carriers are orthogonal to each other, minimizing interference.
Applications: Widely used in modern broadband communications, including Wi-Fi, LTE, and digital television.

### python plot ofdm constellation
python3 ./OFDM/ofdm_constellation.py

Generate Random Data: generate_random_data generates a list of random bits.
QPSK Modulation: qpsk_modulation maps pairs of bits to QPSK symbols. In QPSK, each pair of bits is mapped to a complex symbol with specific in-phase (I) and quadrature (Q) components.
Plot Constellation: plot_constellation plots the complex symbols on a 2D plane to visualize the constellation diagram.

### python modulate ofdm
python3 ./OFDM/modulate_ofdm.py

make sure you install: pip install scipy

you can modulate data to see the effects of OFDM. We'll expand the previous example by including the steps for OFDM modulation. Specifically, we'll perform the following steps:

    Generate random data bits.
    Perform QPSK modulation on the data bits.
    Map the QPSK symbols to OFDM subcarriers.
    Perform IFFT to convert the frequency domain symbols to time domain.
    Add a cyclic prefix.
    Plot the time domain signal and the constellation diagram.

    This code demonstrates the basic process of creating an OFDM signal. Here's a step-by-step explanation:

    Generate Random Data: A function generates random bits.
    QPSK Modulation: The random bits are modulated using QPSK, converting bits into complex symbols.
    Perform IFFT: The IFFT is applied to the QPSK symbols to create the OFDM time-domain signal.
    Add Cyclic Prefix: A cyclic prefix is added to the beginning of each OFDM symbol to mitigate inter-symbol interference (ISI).

## OFDM theoretical introduction
Orthogonal Frequency-Division Multiplexing (OFDM) is a digital multi-carrier modulation method used widely in broadband communications across various standards, including Wi-Fi, LTE, and digital television broadcasting. The key advantages and features of OFDM are rooted in its ability to cope with severe channel conditions—like multipath propagation and frequency-selective fading—without complex equalization filters. Here's a simple theoretical introduction to OFDM:

### 1. Concept of OFDM:
OFDM works by splitting the data stream into multiple smaller streams that are transmitted simultaneously at different frequencies. This approach utilizes the spectrum efficiently and increases the data rate.

### 2. Orthogonality:
The core principle of OFDM is the orthogonality of the sub-carriers. This means that the sub-carriers are spaced in such a way that their peak points align with the null points of the other sub-carriers, thus minimizing interference between them. This spacing allows for the overlap of sub-carriers in the frequency domain, leading to efficient use of bandwidth.

### 3. Structure of OFDM Signal:
- **Sub-carriers**: The total bandwidth is divided into several orthogonal sub-carriers, each carrying a part of the user's data.
- **IFFT/FFT**: Inverse Fast Fourier Transform (IFFT) is used at the transmitter to modulate the data onto the sub-carriers. At the receiver, Fast Fourier Transform (FFT) is used to demodulate the data.
  
### 4. Guard Interval and Cyclic Prefix:
To reduce interference and further enhance robustness against timing errors and multipath effects, OFDM systems incorporate a guard interval between symbols, often filled with a cyclic prefix. The cyclic prefix is a copy of the end of the symbol that is appended to its beginning. This redundancy helps in combating the intersymbol interference (ISI) caused by multipath propagation.

### 5. Benefits of OFDM:
- **Efficient Spectrum Use**: Due to the overlapping of sub-carriers, OFDM is very bandwidth efficient.
- **Robustness to Echoes and Interference**: The cyclic prefix helps in handling echoes and interference from various paths in a multipath environment.
- **Simplified Equalizers**: Due to the use of FFT and the cyclic prefix, OFDM systems can use simple frequency-domain equalizers, which are less complex compared to time-domain equalizers used in traditional single-carrier systems.

### 6. Applications:
OFDM has been adopted in many wireless and wired communication standards, such as IEEE 802.11 (Wi-Fi), LTE (4G), and ADSL broadband Internet. It's favored for its efficiency and performance in environments where channel conditions can be challenging.

Understanding OFDM requires a grasp of Fourier Transform principles and knowledge of signal processing techniques, but the above points provide a basic theoretical introduction.