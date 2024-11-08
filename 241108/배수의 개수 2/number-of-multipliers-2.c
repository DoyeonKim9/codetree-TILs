#include <stdio.h>

int main() {
    int n, cnt = 0;


    for (int i = 1; i <= 10; i++ ) {
        scanf("%d", &n);
        if (n % 2 == 1) {
            cnt++;
        }
    }
    printf("%d", cnt);
    return 0;
}