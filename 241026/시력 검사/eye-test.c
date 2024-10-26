#include <stdio.h>

int main() {
    double r, l;
    scanf("%lf\n%lf", &r, &l);

    if (r >= 1.0 && l >= 1.0) {
        printf("High");
    }
    else if (r >= 0.5 && l >= 0.5) {
        printf("Middle");
    }
    else {
        printf("Low");
    }

    return 0;
}