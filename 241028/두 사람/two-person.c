#include <stdio.h>

int main() {
    int age1, age2;
    char gen1, gen2;
    scanf("%d %c\n", &age1, &gen1);
    scanf("%d %c", &age2, &gen2);

    if (age1 >= 19 && gen1 == 'M' || age2 >= 19 && gen2 == 'M') {
        printf("1");
    }
    else {
        printf("0");
    }
    return 0;
}