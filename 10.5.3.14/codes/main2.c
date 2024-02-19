#include <stdio.h>

int main() {
    // Define variables
    int n;
    float y[25] = {0};
    float x[25] = {0};

    // Calculate y(n) using the given difference equation
    for (n = 1; n < 25; n++) {
        y[n] = y[n-1] + (2*n + 1);
    }

    // Calculate x(n) using the difference equation x(n) = y(n) - y(n-1)
    for (n = 1; n < 25; n++) {
        x[n] = y[n] - y[n-1];
    }

    // Write values to the file
    FILE *fp;
    fp = fopen("values.dat", "w");
    if (fp == NULL) {
        printf("Error opening the file.\n");
        return -1;
    }

    fprintf(fp, "n\tx(n)\ty(n)\n");
    for (n = 0; n < 25; n++) {
        fprintf(fp, "%d\t%.2f\t%.2f\n", n, x[n], y[n]);
    }

    fclose(fp);
    return 0;
}

