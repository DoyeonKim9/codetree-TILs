#include <stdio.h>

int main() {
    char c;
    double a, b;
    scanf("%c\n%lf\n%lf", &c, &a, &b);
    printf("%c\n%.2lf\n%.2lf", c, a, b);
    return 0;
}