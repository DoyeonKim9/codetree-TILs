#include <stdio.h>

int main() {
    int am, ae, bm, be;
    scanf("%d %d\n", &am, &ae);
    scanf("%d %d", &bm, &be);

    if (am > bm){
        printf("A");
    }
    else if (am == bm && ae > be) {
        printf("A");
    }
    else{
        printf("B");
    }

    return 0;
}