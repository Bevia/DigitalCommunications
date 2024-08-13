
## How to run:
    g++ ./DSSS/dsss_.cpp ./DSSS/dsss_.cpp -o dsss_ 
### To enable C++11, use the following command:
    g++ -std=c++11 ./DSSS/dsss_.cpp -o ./DSSS/dsss_.cpp -o dsss_ 
#### To run the program, use this command:
    ./dsss_


## DSSS Theory
Direct Sequence Spread Spectrum (DSSS) is a technique used in telecommunications where the data signal is spread over a wider bandwidth by multiplying it with a pseudo-random noise (PN) sequence, also known as a spreading code. This increases the signal's resistance to interference and eavesdropping.

Spread Spectrum Techniques:

Direct Sequence Spread Spectrum (DSSS): Data is spread over a wide frequency band by multiplying the signal with a pseudo-random noise code.
Frequency Hopping Spread Spectrum (FHSS): The carrier frequency hops among many frequencies according to a pseudo-random sequence.
Applications: Used in military communications, GPS, and some wireless LAN technologies (e.g., early versions of Wi-Fi).

### Code explanation
Explanation

### Generate Random Data:
    The generate_random_data function generates a sequence of random binary data (0s and 1s).

### Generate PN Sequence:
    The generate_pn_sequence function generates a pseudo-random noise sequence of the same length as the data sequence. In this example, the PN sequence is generated with values of either 1 or -1 to accommodate Binary Phase Shift Keying (BPSK) modulation.

### Spread the Data:
    The spread_data function multiplies each bit of the data with the entire PN sequence. If the data bit is 1, the PN sequence is used as is; if the data bit is 0, the PN sequence is inverted.

### Main Function:
    The main function generates the data and PN sequence, spreads the data, and then prints out the original data, the PN sequence, and the spread signal.