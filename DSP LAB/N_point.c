#include <stdio.h>
#include <stdlib.h>
#include <complex.h>
#include <math.h>
#define PI 3.14159265358979323846
double complex twiddle_factor(int N, int k) {
    return cexp(-2.0 * I * PI * k / N);
}
void fft_2point(double complex* x, double complex* X) {
    X[0] = x[0] + x[1];
    X[1] = x[0] - x[1];
}
void fft_recursive(double complex* x, double complex* X, int N) {
    if (N == 2) {
        fft_2point(x, X);
    } else {
        double complex even[N/2], odd[N/2];
        for (int i = 0; i < N/2; i++) {
            even[i] = x[2*i];
            odd[i] = x[2*i + 1];
        }
        double complex even_fft[N/2], odd_fft[N/2];
        fft_recursive(even, even_fft, N/2);
        fft_recursive(odd, odd_fft, N/2);
        for (int k = 0; k < N/2; k++) {
            X[k] = even_fft[k] + twiddle_factor(N, k) * odd_fft[k];
            X[k + N/2] = even_fft[k] - twiddle_factor(N, k) * odd_fft[k]; } } }
int main() {
   int N;
    printf("Enter the value of N: ");
    scanf("%d", &N);
    double complex x[N];
    printf("Enter the %d elements of the sequence:\n", N);
    for (int i = 0; i < N; i++) {
        double real_part;
        scanf("%lf", &real_part);
        x[i] = real_part + 0 * I; // Assuming real input, set imaginary part to 0
    }
    double complex X[N];
    fft_recursive(x, X, N);
    printf("N-point FFT:\n");
    for (int i = 0; i < N; i++) {
        printf("X[%d] = %.2f%+.2fi\n", i, creal(X[i]), cimag(X[i]));
    }
    return 0;
}