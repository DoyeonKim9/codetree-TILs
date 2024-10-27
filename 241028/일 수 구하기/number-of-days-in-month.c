#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    if (n == 2) {
        printf("28");
    }
    else if (n < 8) {
        if (n % 2 == 1) {
            printf("31");
        }
        else {
            printf("30");
        }
    }
    else {
        if (n % 2 == 1) {
            printf("30");
        }
        else {
            printf("31");
        }
    }
    return 0;
}