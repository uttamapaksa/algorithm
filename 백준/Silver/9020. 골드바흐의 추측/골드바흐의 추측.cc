#include <stdio.h>
#include <stdbool.h>
#define MAX 10000

int main() {
    bool P[MAX];
    for (int i = 0; i < MAX; i++) {
        P[i] = true;
    }
    for (int i = 2; i * i < MAX; i++) {
        for (int j = i * i; j < MAX; j += i) {
            if (P[j]) {
                P[j] = false;
            }
        }
    }

    int T;
    scanf("%d", &T);
    while (T--) {
        int n;
        scanf("%d", &n);
        for (int i = n / 2; i > 1; i--) {
            if (P[i] && P[n - i]) {
                printf("%d %d\n", i, n - i);
                break;
            }
        }
    }

    return 0;
}