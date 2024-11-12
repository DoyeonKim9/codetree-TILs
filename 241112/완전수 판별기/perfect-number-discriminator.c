#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    int sum_val = 0;

    for (int i = 1; i < n; i++) {
        if (n % i == 0)
            sum_val += i;
    }
    if (sum_val == n)
        printf("P");
    else
        printf("N");
    return 0;
}