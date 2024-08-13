#include <iostream>
#include <vector>
#include <random>
#include <ctime>

// Function to generate random binary data (0 or 1)
std::vector<int> generate_random_data(int length) {
    std::vector<int> data(length);
    std::mt19937 gen(static_cast<unsigned int>(std::time(0)));
    std::uniform_int_distribution<> dis(0, 1);

    for (int i = 0; i < length; ++i) {
        data[i] = dis(gen);
    }

    return data;
}

// Function to generate a PN sequence (spreading code)
std::vector<int> generate_pn_sequence(int length) {
    std::vector<int> pn_sequence(length);
    std::mt19937 gen(static_cast<unsigned int>(std::time(0)));
    std::uniform_int_distribution<> dis(0, 1);

    for (int i = 0; i < length; ++i) {
        pn_sequence[i] = dis(gen) ? 1 : -1; // Map 0 to -1 for BPSK spreading
    }

    return pn_sequence;
}

// Function to spread the data using the PN sequence
std::vector<int> spread_data(const std::vector<int>& data, const std::vector<int>& pn_sequence) {
    std::vector<int> spread_signal(data.size() * pn_sequence.size());

    for (size_t i = 0; i < data.size(); ++i) {
        for (size_t j = 0; j < pn_sequence.size(); ++j) {
            spread_signal[i * pn_sequence.size() + j] = data[i] == 0 ? -pn_sequence[j] : pn_sequence[j];
        }
    }

    return spread_signal;
}

int main() {
    // Parameters
    const int data_length = 8;  // Length of the binary data sequence
    const int pn_length = 8;    // Length of the PN sequence

    // Generate random binary data
    std::vector<int> data = generate_random_data(data_length);

    // Generate PN sequence (spreading code)
    std::vector<int> pn_sequence = generate_pn_sequence(pn_length);

    // Spread the data using the PN sequence
    std::vector<int> spread_signal = spread_data(data, pn_sequence);

    // Output the results
    std::cout << "Original Data: ";
    for (int bit : data) {
        std::cout << bit << " ";
    }
    std::cout << std::endl;

    std::cout << "PN Sequence: ";
    for (int bit : pn_sequence) {
        std::cout << bit << " ";
    }
    std::cout << std::endl;

    std::cout << "Spread Signal: ";
    for (int bit : spread_signal) {
        std::cout << bit << " ";
    }
    std::cout << std::endl;

    return 0;
}
