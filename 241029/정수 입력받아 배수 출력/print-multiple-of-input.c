#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    for (int i = n; i <= n*5; i += n) {
        printf("%d ", i);
    }
    return 0;
}