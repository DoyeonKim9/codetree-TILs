#include <stdio.h>

int main() {
    int m1, m2, e1, e2;
    scanf("%d %d\n", &m1, &e1);
    scanf("%d %d", &m2, &e2);

    if (m1 > m2 && e1 > e2) {
        printf("1");
    }
    else {
        printf("0");
    }
    return 0;
}