#include <stdio.h>
#include <complex.h>
#include <math.h>
void butterfly(complex double *x1, complex double *x2, int N, int k) {
    complex double w = cexp(-I * 2 * 3.1415 * k / N);
    complex double temp = *x2;
    printf("a=%f b=%f", N, k);
    *x2 = *x1 - w * temp;
    *x1 = *x1 + w * temp;
}

int main() {
    complex double x1, x2;
    int N, k;

    printf("Enter the two numbers a,b: ");
    double real_x1, imag_x1, real_x2, imag_x2;
    scanf("%f %f %f %f", &real_x1, &imag_x1, &real_x2, &imag_x2);

    printf("Enter the input size (N): ");
    scanf("%d", &N);

    printf("Enter the stage index (k): ");
    scanf("%d", &k);

    butterfly(&x1, &x2, N, k);

    printf("Butterfly result: x1 = %.2f + %.2fi, x2 = %.2f + %.2fi\n", creal(x1), cimag(x1), creal(x2), cimag(x2));

    return 0;
}