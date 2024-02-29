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
    for (y = 0; y <= 5; y += 1) {
        f = sqrt((pow(10, ((20 - y) / 10.0)) - 1) / (pow(10, -8) * 4 * pow(M_PI, 2)));
        fprintf(fp, "%.2f %.2f\n", f, y);
    }

    fclose(fp);
    return 0;
}

