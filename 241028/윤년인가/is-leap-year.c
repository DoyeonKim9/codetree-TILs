#include <stdio.h>

int main() {
    int y;
    scanf("%d", &y);

    if ((y % 4 == 0 && y % 100 != 0) || y % 400 == 0) {
        printf("true");
    }
    else {
        printf("false");
    }
    return 0;
}