#include <iostream>
#include <vector>
#include <complex>
#include <cmath>
#include <fftw3.h>
#include <random>

using namespace std;

// Function to generate random data bits
vector<int> generate_random_data(int num_bits) {
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(0, 1);
    vector<int> data(num_bits);
    for (int i = 0; i < num_bits; ++i) {
        data[i] = dis(gen);
    }
    return data;
}

// Function to perform QPSK modulation
vector<complex<double>> qpsk_modulation(const vector<int>& data) {
    vector<complex<double>> modulated_data(data.size() / 2);
    for (size_t i = 0; i < data.size(); i += 2) {
        double real = (data[i] == 0) ? 1.0 : -1.0;
        double imag = (data[i + 1] == 0) ? 1.0 : -1.0;
        modulated_data[i / 2] = {real, imag};
    }
    return modulated_data;
}

// Function to perform IFFT
vector<complex<double>> perform_ifft(const vector<complex<double>>& data) {
    int N = data.size();
    fftw_complex *in = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * N);
    fftw_complex *out = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * N);
    fftw_plan p = fftw_plan_dft_1d(N, in, out, FFTW_BACKWARD, FFTW_ESTIMATE);

    for (int i = 0; i < N; ++i) {
        in[i][0] = data[i].real();
        in[i][1] = data[i].imag();
    }

    fftw_execute(p);

    vector<complex<double>> ifft_data(N);
    for (int i = 0; i < N; ++i) {
        ifft_data[i] = {out[i][0] / N, out[i][1] / N};
    }

    fftw_destroy_plan(p);
    fftw_free(in);
    fftw_free(out);

    return ifft_data;
}

// Function to add cyclic prefix
vector<complex<double>> add_cyclic_prefix(const vector<complex<double>>& data, int cp_len) {
    int N = data.size();
    vector<complex<double>> cp_data(cp_len + N);
    for (int i = 0; i < cp_len; ++i) {
        cp_data[i] = data[N - cp_len + i];
    }
    for (int i = 0; i < N; ++i) {
        cp_data[cp_len + i] = data[i];
    }
    return cp_data;
}

int main() {
    // Parameters
    const int num_subcarriers = 64;
    const int cp_len = 16;

    // Generate random data
    vector<int> data = generate_random_data(num_subcarriers * 2);

    // Perform QPSK modulation
    vector<complex<double>> modulated_data = qpsk_modulation(data);

    // Perform IFFT
    vector<complex<double>> ifft_data = perform_ifft(modulated_data);

    // Add cyclic prefix
    vector<complex<double>> tx_signal = add_cyclic_prefix(ifft_data, cp_len);

    // Output the transmitted signal
    cout << "Transmitted OFDM signal with cyclic prefix:" << endl;
    for (const auto& sample : tx_signal) {
        cout << sample << endl;
    }

    return 0;
}