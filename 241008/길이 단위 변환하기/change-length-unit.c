#include <stdio.h>

int main() {
    double a = 30.48, b = 160934;
    double A = 9.2, B = 1.3;
    double c = a*A, C = b*B;

    printf("%.1lfft = %.1lfcm \n", A, c );
    printf("%.1lfmi = %.1lfcm \n", B, C);
    return 0;
}