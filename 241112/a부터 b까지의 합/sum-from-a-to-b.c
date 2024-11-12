#include <stdio.h>

int main() {
    int a, b;
    scanf("%d %d", &a, &b);
    int sum_val = 0;
    for (int i = a; i <= b; i++) {
        sum_val += i;
    }
    printf("%d", sum_val);
    return 0;
}