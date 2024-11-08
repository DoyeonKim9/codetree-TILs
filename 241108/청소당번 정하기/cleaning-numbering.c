#include <stdio.h>

int main() {
    int n;
    int cnt2 = 0, cnt3 = 0, cnt12 = 0;
    scanf("%d", &n);

    for(int i = 1; i <= n; i++){
        if (i % 12 == 0)
            cnt12++;
        else if (i % 3 == 0)
            cnt3++;
        else if (i % 2 == 0)
            cnt2++;
    }
    printf("%d %d %d", cnt2, cnt3, cnt12);
    return 0;
}