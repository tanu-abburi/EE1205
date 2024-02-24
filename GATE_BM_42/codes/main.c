#include <stdio.h>
#include <math.h>

double g(double t) {
    return -14 * exp(-8 * t) + 3 * exp(-4 * t);
}

int main() {
    FILE *fp;
    fp = fopen("values.dat", "w");
    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    double t = 0.0;
    while (t <= 10.0) { // Adjust the upper limit as needed
        double value = g(t);
        fprintf(fp, "%lf\n", value);
        t += 0.1; // Adjust the step size as needed
    }

    fclose(fp);
    return 0;
}

