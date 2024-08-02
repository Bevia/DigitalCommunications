#include <iostream>
#include <complex>
#include <vector>

// Define the QPSK symbols using complex numbers
const std::complex<double> QPSK_SYMBOLS[4] = {
    std::complex<double>(1, 1),   // 00
    std::complex<double>(-1, 1),  // 01
    std::complex<double>(-1, -1), // 11
    std::complex<double>(1, -1)   // 10
};

// Function to map bit pairs to QPSK symbols
std::complex<double> bitsToQPSKSymbol(int bit1, int bit2) {
    int index = (bit1 << 1) | bit2;
    return QPSK_SYMBOLS[index];
}

// Function to map QPSK symbols back to bit pairs
std::pair<int, int> qpskSymbolToBits(const std::complex<double>& symbol) {
    int bit1 = symbol.real() < 0 ? 1 : 0;
    int bit2 = symbol.imag() < 0 ? 1 : 0;
    return {bit1, bit2};
}

int main() {
    // Example bit stream to be transmitted
    std::vector<int> bitStream = {1, 1, 0, 1, 0, 0, 1, 0};
    std::vector<std::complex<double>> modulatedSignal;

    // Modulate the bit stream using QPSK
    for (size_t i = 0; i < bitStream.size(); i += 2) {
        int bit1 = bitStream[i];
        int bit2 = bitStream[i + 1];
        std::complex<double> symbol = bitsToQPSKSymbol(bit1, bit2);
        modulatedSignal.push_back(symbol);
    }

    // Print the modulated signal
    std::cout << "Modulated Signal:" << std::endl;
    for (const auto& symbol : modulatedSignal) {
        std::cout << symbol << " ";
    }
    std::cout << std::endl;

    // Demodulate the signal back to bits
    std::vector<int> demodulatedBits;
    for (const auto& symbol : modulatedSignal) {
        auto [bit1, bit2] = qpskSymbolToBits(symbol);
        demodulatedBits.push_back(bit1);
        demodulatedBits.push_back(bit2);
    }

    // Print the demodulated bits
    std::cout << "Demodulated Bits:" << std::endl;
    for (const auto& bit : demodulatedBits) {
        std::cout << bit << " ";
    }
    std::cout << std::endl;

    return 0;
}
