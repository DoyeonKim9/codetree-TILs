#include <stdio.h>

int main() {
    int a = 1, b = 2, c = 3;
    int sum;
    sum = a + b + c;
    a = b = c = sum;
    printf("%d %d %d", a, b, c);
    return 0;
}