#include <stdio.h>

int main() {
    int a, b;
    scanf("%d\n%d", &a, &b);

    a += 87;
    printf("%d\n", a);
    printf("%d", b % 10);

    return 0;
}