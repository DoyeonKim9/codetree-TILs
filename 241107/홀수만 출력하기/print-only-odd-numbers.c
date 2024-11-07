#include <stdio.h>

int main() {
    int n, a;
    scanf("%d\n", &n);
    
    for (int i = 1; i <= n; i++){
        scanf("%d\n", &a);
        if (a % 3 == 0 && a % 2 == 1)
            printf("%d\n", a);
    }
    return 0;
}