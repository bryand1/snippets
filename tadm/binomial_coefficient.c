#include <stdio.h>

#define MAXN 100

long binomial_coefficient(int n, int m) {
    int i, j;
    long bc[MAXN][MAXN];
    for (i = 0; i <= n; i++) bc[i][0] = 1;
    for (j = 1; j <= n; j++) bc[j][j] = 1;
    for (i = 2; i <= n; i++)
        for (j = 1; j < i; j++)
            bc[i][j] = bc[i - 1][j - 1] + bc[i - 1][j];
    return bc[n][m];
}

int main(void) {
    printf("%ld %ld %ld %ld %ld %ld\n",
        binomial_coefficient(5, 0),
        binomial_coefficient(5, 1),
        binomial_coefficient(5, 2),
        binomial_coefficient(5, 3),
        binomial_coefficient(5, 4),
        binomial_coefficient(5, 5));
    return 0;
}
