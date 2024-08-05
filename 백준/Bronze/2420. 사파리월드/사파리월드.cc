#include <stdio.h>

int main() {
    long long N, M, res;
    scanf("%lld %lld", &N, &M);
    
    if (N < M) {
        res = M - N;
    } else {
        res = N - M;
    }
    
    printf("%lld\n", res);
    return 0;
}
