#include <stdio.h>

#define N 27 // Range from 0 to 26

// Step function u(n)
int step(int n) {
    return (n >= 0) ? 1 : 0;
}

// Function y(n) = (n^2 + 2n + 1) * u(n)
int y(int n) {
    return (n * n + 2 * n + 1) * step(n);
}

int main() {
    FILE *fp;
    fp = fopen("values.dat", "w");

    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    for (int n = 0; n < N; n++) {
        fprintf(fp, "%d\n", y(n));
    }

    fclose(fp);

    return 0;
}

