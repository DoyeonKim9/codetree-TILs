#include <stdio.h>

int main() {
    int a, b;
    scanf("%d %d", &a, &b);
    double c;
    c = (double) (a + b) / (a - b);
    printf("%.2lf", c);
    return 0;
}