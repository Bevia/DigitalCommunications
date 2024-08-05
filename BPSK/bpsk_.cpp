#include <iostream>
#include <vector>
#include <cmath>
#include <random>
#include <complex>

// Constants
const double PI = 3.14159265358979323846;
const double CARRIER_FREQ = 1000.0; // Carrier frequency in Hz
const double SAMPLE_RATE = 10000.0; // Sampling rate in Hz
const int SAMPLES_PER_SYMBOL = 100; // Number of samples per symbol
const double NOISE_STD_DEV = 0.1;   // Standard deviation of Gaussian noise

// Generate a binary data sequence
std::vector<int> generateBinaryData(int length) {
    std::vector<int> data(length);
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(0, 1);
    for (int i = 0; i < length; ++i) {
        data[i] = dis(gen);
    }
    return data;
}

// BPSK Modulation
std::vector<std::complex<double>> bpskModulate(const std::vector<int>& data) {
    std::vector<std::complex<double>> modulatedSignal;
    for (int bit : data) {
        double phase = (bit == 0) ? 0.0 : PI;
        for (int i = 0; i < SAMPLES_PER_SYMBOL; ++i) {
            double t = i / SAMPLE_RATE;
            double sample = std::cos(2 * PI * CARRIER_FREQ * t + phase);
            modulatedSignal.push_back({sample, 0.0});
        }
    }
    return modulatedSignal;
}

// Add Gaussian noise to the signal
void addNoise(std::vector<std::complex<double>>& signal) {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::normal_distribution<> dis(0.0, NOISE_STD_DEV);
    for (auto& sample : signal) {
        sample.real(sample.real() + dis(gen));
    }
}

// BPSK Demodulation
std::vector<int> bpskDemodulate(const std::vector<std::complex<double>>& signal) {
    std::vector<int> demodulatedData;
    for (size_t i = 0; i < signal.size(); i += SAMPLES_PER_SYMBOL) {
        double correlation = 0.0;
        for (int j = 0; j < SAMPLES_PER_SYMBOL; ++j) {
            double t = j / SAMPLE_RATE;
            double reference = std::cos(2 * PI * CARRIER_FREQ * t);
            correlation += signal[i + j].real() * reference;
        }
        demodulatedData.push_back((correlation > 0) ? 0 : 1);
    }
    return demodulatedData;
}

int main() {
    // Generate binary data
    int dataLength = 10;
    std::vector<int> data = generateBinaryData(dataLength);

    // Display original data
    std::cout << "Original data: ";
    for (int bit : data) {
        std::cout << bit << " ";
    }
    std::cout << std::endl;

    // Modulate the data using BPSK
    std::vector<std::complex<double>> modulatedSignal = bpskModulate(data);

    // Add noise to the modulated signal
    addNoise(modulatedSignal);

    // Demodulate the received signal
    std::vector<int> demodulatedData = bpskDemodulate(modulatedSignal);

    // Display demodulated data
    std::cout << "Demodulated data: ";
    for (int bit : demodulatedData) {
        std::cout << bit << " ";
    }
    std::cout << std::endl;

    return 0;
}
