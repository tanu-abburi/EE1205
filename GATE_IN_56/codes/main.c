#include <stdio.h>
#include <math.h>

int main() {
    FILE *fp;
    fp = fopen("values.dat", "w");

    if (fp == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    double f, y;
    for (f = 0; f <= 20e3; f += 100) { // Incrementing by 100 Hz
        y = 20 - 10 * log10(pow(f, 2) * pow(10, -8) * 4 * pow(M_PI, 2) + 1);
        fprintf(fp, "%.2f %.2f\n", f, y);
    }

    fclose(fp);
    return 0;
}

