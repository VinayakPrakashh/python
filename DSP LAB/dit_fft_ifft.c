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

void fft(complex *x, int N) {
    bit_reverse(x, N);
    for (int s = 1; s <= log2(N); s++) {
        int m = 1 << s;
        int m2 = m >> 1;
        complex w_m = twiddle_factor(m);
        for (int k = 0; k < N; k += m) {
            complex w = {1.0, 0.0};
            for (int j = 0; j < m2; j++) {
                complex t = mul(w, x[k + j + m2]);
                complex u = x[k + j];
                x[k + j] = add(u, t);
                x[k + j + m2] = sub(u, t);
                w = mul(w, w_m);
            }
        }
    }
}
void ifft(complex *x, int N) {
    bit_reverse(x, N);
    for (int s = 1; s <= log2(N); s++) {
        int m = 1 << s;
        int m2 = m >> 1;
        complex w_m = twiddle_factor_2(m);
        for (int k = 0; k < N; k += m) {
            complex w = {1.0, 0.0};
            for (int j = 0; j < m2; j++) {
                complex t = mul(w, x[k + j + m2]);
                complex u = x[k + j];
                x[k + j] = add(u, t);
                x[k + j + m2] = sub(u, t);
                w = mul(w, w_m);
            }
        }
    }
    for (int i = 0; i < N; i++) {
            x[i].real /= N;
            x[i].imag /= N;
        }
}
int main() {
    int N = 16;
    complex x[16] = {{0.0, 0.0}, {1.0, 0.0}, {2.0, 0.0}, {3.0, 0.0}, {4.0, 0.0}, {5.0, 0.0}, {6.0, 0.0}, {7.0, 0.0}, {8.0, 0.0}, {9.0, 0.0}, {10.0, 0.0}, {11.0, 0.0}, {12.0, 0.0}, {13.0, 0.0}, {14.0, 0.0}, {15.0, 0.0}};
    
    fft(x, N);
    ifft(x, N);
    for (int i = 0; i < N; i++) {
        print_complex(x[i]);
    }
    
    return 0;
}