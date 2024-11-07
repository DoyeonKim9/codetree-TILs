#include <stdio.h>

int main() {
    int a, b;
    scanf("%d %d", &a, &b);

    printf("%d ", a);
    for (int i = a; i <= b;) {
        if (i % 2 == 1)
            i = i * 2;
        else 
            i += 3;
        if (i > b)
            break;
        printf("%d ", i);

    }
    return 0;

}