#include <iostream>
#include <vector>
#include <complex>
#include <cmath>

// Define QAM parameters
const int M = 16; // 16-QAM
const int k = std::log2(M); // Bits per symbol
const double pi = 3.14159265358979323846;

// Generate QAM constellation points
std::vector<std::complex<double>> generateQAMConstellation(int M) {
    std::vector<std::complex<double>> constellation;
    int m_sqrt = std::sqrt(M);
    for (int i = 0; i < m_sqrt; ++i) {
        for (int j = 0; j < m_sqrt; ++j) {
            constellation.push_back({2.0 * i - m_sqrt + 1, 2.0 * j - m_sqrt + 1});
        }
    }
    return constellation;
}

// Map bits to QAM symbols
std::vector<std::complex<double>> modulate(const std::vector<int>& bits, const std::vector<std::complex<double>>& constellation) {
    std::vector<std::complex<double>> symbols;
    for (size_t i = 0; i < bits.size(); i += k) {
        int index = 0;
        for (int j = 0; j < k; ++j) {
            index = (index << 1) | bits[i + j];
        }
        symbols.push_back(constellation[index]);
    }
    return symbols;
}

// Demodulate QAM symbols to bits
std::vector<int> demodulate(const std::vector<std::complex<double>>& symbols, const std::vector<std::complex<double>>& constellation) {
    std::vector<int> bits;
    for (const auto& symbol : symbols) {
        double min_distance = std::numeric_limits<double>::max();
        int closest_index = 0;
        for (size_t i = 0; i < constellation.size(); ++i) {
            double distance = std::norm(symbol - constellation[i]);
            if (distance < min_distance) {
                min_distance = distance;
                closest_index = i;
            }
        }
        for (int j = k - 1; j >= 0; --j) {
            bits.push_back((closest_index >> j) & 1);
        }
    }
    return bits;
}

int main() {
    // Example bits to modulate (must be a multiple of k)
    std::vector<int> bits = {0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0};

    // Generate 16-QAM constellation
    std::vector<std::complex<double>> constellation = generateQAMConstellation(M);

    // Modulate bits to QAM symbols
    std::vector<std::complex<double>> symbols = modulate(bits, constellation);

    // Output modulated symbols
    std::cout << "Modulated symbols:\n";
    for (const auto& symbol : symbols) {
        std::cout << symbol << "\n";
    }

    // Demodulate symbols back to bits
    std::vector<int> demodulated_bits = demodulate(symbols, constellation);

    // Output demodulated bits
    std::cout << "\nDemodulated bits:\n";
    for (const auto& bit : demodulated_bits) {
        std::cout << bit;
    }
    std::cout << std::endl;

    return 0;
}
