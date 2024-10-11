#include <stdio.h>

int main() {
    int a = 5, b = 6, c = 7;
    int temp1, temp2, temp3;
    temp1 = a;
    a = b;
    b = temp1;

    temp3 = c;
    c = a;
    a = temp3;

    printf("%d\n%d\n%d", a, b, c);
    return 0;
}