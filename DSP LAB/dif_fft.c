#include <stdio.h>
#include <math.h>
#define M_PI 3.14159265358979323846
typedef struct {
    double real;
    double imag;
} complex;

complex sub(complex a, complex b) {
    complex c;
    c.real = a.real - b.real;
    c.imag = a.imag - b.imag;
    return c;
}

complex mul(complex a, complex b) {
    complex c;
    c.real = (a.real * b.real) - (a.imag * b.imag);
    c.imag = (a.real * b.imag) + (a.imag * b.real);
    return c;
}

complex add(complex a, complex b) {
    complex c;
    c.real = a.real + b.real;
    c.imag = a.imag + b.imag;
    return c;
}

void print_complex(complex c) {
    if (c.imag >= 0) {
        printf("%.6f + %.6fi\n", c.real, c.imag);
    } else {
        printf("%.6f - %.6fi\n", c.real, -c.imag);
    }
}

complex twiddle_factor(int N) {
    complex w = {cos(2 * M_PI / N), -sin(2 * M_PI / N)};
    return w;
}
complex twiddle_factor_2(int N) {
    complex w = {cos(2 * M_PI / N), sin(2 * M_PI / N)};
    return w;
}
void bit_reverse(complex *x, int N) {
    int i, j, k;
    complex temp;
    for (i = 1, j = 0; i < N; i++) {
        for (k = N >> 1; k > (j ^= k); k >>= 1);
        if (i < j) {
            temp = x[i];
            x[i] = x[j];
            x[j] = temp;
        }
    }
}

void dif_fft(complex *x, int N) {
	int i=1;
	int s=0;
	while(i!=N){
		i=i*2;
		s+=1;
	}

    for (s; s >= 1; s--) { // Outer loop: stages
        int m = 1 << s; // m = 2^s
        int m2 = m >> 1; // m2 = m / 2
        complex w_m = twiddle_factor(m); // Twiddle factor for the current stage
        int k;
        for (k = 0; k < N; k += m) { // Middle loop: groups
            complex w = {1.0, 0.0}; // Initialize w to 1
            int j;
            for (j = 0; j < m2; j++) { // Inner loop: butterflies
                complex u = x[k + j]; // First half
                complex t = x[k + j + m2]; // Second half
                x[k + j] = add(u, t); // Combine first and second half
                x[k + j + m2] = mul(sub(u, t), w); // Apply twiddle factor to the second half
                w = mul(w, w_m); // Update w for the next butterfly
            }
        }
    }
    bit_reverse(x, N); // Bit-reverse the output
}
void dif_ifft(complex *x, int N) {
	int i=1;
	int s=0;
	while(i!=N){
		i=i*2;
		s+=1;
	}
    for (s; s >= 1; s--) { // Outer loop: stages
        int m = 1 << s; // m = 2^s
        int m2 = m >> 1; // m2 = m / 2
        complex w_m = twiddle_factor_2(m); // Twiddle factor for the current stage
        int k;
        for (k = 0; k < N; k += m) { // Middle loop: groups
            complex w = {1.0, 0.0}; // Initialize w to 1
            int j;
            for (j = 0; j < m2; j++) { // Inner loop: butterflies
                complex u = x[k + j]; // First half
                complex t = x[k + j + m2]; // Second half
                x[k + j] = add(u, t); // Combine first and second half
                x[k + j + m2] = mul(sub(u, t), w); // Apply twiddle factor to the second half
                w = mul(w, w_m); // Update w for the next butterfly
            }
        }
    }
    bit_reverse(x, N); // Bit-reverse the output

    for (i = 0; i < N; i++) {
            x[i].real /= N;
            x[i].imag /= N;
        }
}
int main() {
    int N = 8;
    complex x[8] = {{0.0, 0.0}, {1.0, 0.0}, {2.0, 0.0}, {3.0, 0.0}, {4.0, 0.0}, {5.0, 0.0}, {6.0, 0.0}, {7.0, 0.0}};
    // bit_reverse(x, N);
    dif_fft(x, N);
    dif_ifft(x, N);
    int i;
    for (i = 0; i < N; i++) {
        print_complex(x[i]);
    }

    return 0;
}
