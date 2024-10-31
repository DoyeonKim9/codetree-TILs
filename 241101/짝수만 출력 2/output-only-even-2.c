#include <stdio.h>

int main() {
    int b, a;
    scanf("%d %d", &b, &a);
    int i = b;

    while (i >= a) {
        printf("%d ", i);
        i -= 2;
    }
    return 0;
}