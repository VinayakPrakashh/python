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
    int i=1;
    	int S=0;
    	while(i!=N){
    		i=i*2;
    		S+=1;
    	}
    	int s;
    for (s = 1; s <= S; s++) {
        int m = 1 << s;
        int m2 = m >> 1;
        complex w_m = twiddle_factor(m);
        int k;
        for (k = 0; k < N; k += m) {
            complex w = {1.0, 0.0};
            int j;
            for (j = 0; j < m2; j++) {
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
    int i=1;
    	int S=0;
    	while(i!=N){
    		i=i*2;
    		S+=1;
    	}
    	int s;
    	int k;
    for ( s = 1; s <= S; s++) {
        int m = 1 << s;
        int m2 = m >> 1;
        complex w_m = twiddle_factor_2(m);

        for (k = 0; k < N; k += m) {
            complex w = {1.0, 0.0};
            int j;
            for (j = 0; j < m2; j++) {
                complex t = mul(w, x[k + j + m2]);
                complex u = x[k + j];
                x[k + j] = add(u, t);
                x[k + j + m2] = sub(u, t);
                w = mul(w, w_m);
            }
        }
    }
