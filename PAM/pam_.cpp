#include <iostream>
#include <vector>
#include <cmath>
#include <random>
#include <iomanip>

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

// Function to perform Pulse Amplitude Modulation (PAM)
std::vector<double> pam_modulation(const std::vector<int>& data, int M) {
    std::vector<double> modulated_data(data.size());

    // Assume M-PAM where M = 2^k (e.g., M=2 for Binary PAM, M=4 for 4-PAM)
    double amplitude_step = 2.0 / (M - 1); // Normalize amplitude between -1 and 1

    for (size_t i = 0; i < data.size(); ++i) {
        // Modulate the data: map 0 to -1 and 1 to 1 for binary PAM (M=2)
        modulated_data[i] = -1 + data[i] * amplitude_step * (M - 1);
    }

    return modulated_data;
}

// Function to print the modulated signal
void print_modulated_signal(const std::vector<double>& modulated_data) {
    std::cout << "PAM Modulated Signal: ";
    for (double sample : modulated_data) {
        std::cout << std::fixed << std::setprecision(2) << sample << " ";
    }
    std::cout << std::endl;
}

int main() {
    // Parameters
    const int data_length = 8;  // Length of the binary data sequence
    const int M = 2;            // PAM order (M=2 for Binary PAM, M=4 for 4-PAM, etc.)

    // Generate random binary data
    std::vector<int> data = generate_random_data(data_length);

    // Perform PAM modulation
    std::vector<double> modulated_data = pam_modulation(data, M);

    // Output the results
    std::cout << "Original Data: ";
    for (int bit : data) {
        std::cout << bit << " ";
    }
    std::cout << std::endl;

    print_modulated_signal(modulated_data);

    return 0;
}
