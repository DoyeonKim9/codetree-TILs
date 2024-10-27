#include <stdio.h>

int main() {
    int m;
    scanf("%d", &m);

    if (m >= 12 || m <= 2) {
        printf("Winter");
    }
    else if (m <= 5) {
        printf("Spring");
    }
    else if (m <= 8) {
        printf("Summer");
    }
    else {
        printf("Fall");
    }
    return 0;
}