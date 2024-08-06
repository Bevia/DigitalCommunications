
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

### python plot ofdm constellation
python3 ./OFDM/ofdm_constellation.py

Generate Random Data: generate_random_data generates a list of random bits.
QPSK Modulation: qpsk_modulation maps pairs of bits to QPSK symbols. In QPSK, each pair of bits is mapped to a complex symbol with specific in-phase (I) and quadrature (Q) components.
Plot Constellation: plot_constellation plots the complex symbols on a 2D plane to visualize the constellation diagram.

### python modulate ofdm
python3 ./OFDM/modulate_ofdm.py

you can modulate data to see the effects of OFDM. We'll expand the previous example by including the steps for OFDM modulation. Specifically, we'll perform the following steps:

    Generate random data bits.
    Perform QPSK modulation on the data bits.
    Map the QPSK symbols to OFDM subcarriers.
    Perform IFFT to convert the frequency domain symbols to time domain.
    Add a cyclic prefix.
    Plot the time domain signal and the constellation diagram.