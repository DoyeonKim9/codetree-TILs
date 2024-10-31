#include <stdio.h>

int main() {
    int n;
    int i = 3;
    scanf("%d", &n);
   
    while (i <= n) {
        printf("%d ", i);
        i += 3;
    }
    return 0;
}