#include <stdio.h>

int main() {
    int mid, fin;
    scanf("%d %d", &mid, &fin);

    if (mid >= 90 && fin >= 95){
        printf("100000");
    }
    else if (mid >= 90 && fin >= 90) {
        printf("50000");
    }
    else{
        printf("0");
    }
    return 0;
}