
## How to run:
    g++ ./OFDM/ofdm_.cpp ./OFDM/ofdm_.cpp -o ofdm 
### To enable C++11, use the following command:
    g++ -std=c++11 ./OFDM/ofdm_.cpp -o ./OFDM/ofdm_.cpp -o ofdm 
#### To run the program, use this command:
    ./ftir

### compile the FTTW3 library...find the route of the lib and do the following:
g++ -std=c++11 -o ofdm_ ./OFDM/ofdm_.cpp -lfftw3 -L/opt/homebrew/Cellar/fftw/3.3.10_1/lib/ -I/opt/homebrew/Cellar/fftw/3.3.10_1/include
