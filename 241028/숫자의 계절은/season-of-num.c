#include <stdio.h>

int main() {
    int m;
    scanf("%d", &m);

    if (m >= 12 || m <= 2) {
        printf("Winter");
    }
    else if (m > 5) {
        printf("Summer");
    }
    else if (m > 2) {
        printf("Spring");
    }
    else {
        printf("Fall");
    }
    return 0;
}