#include <stdio.h>

double a(double t) {
    return (-0.5 * t + 10) / 10;
}

int main() {
    FILE *fp;
    fp = fopen("values.dat", "w");
    if (fp == NULL) {
        printf("Error opening file.\n");
        return 1;
    }
    
    for (int t = 0; t <= 10; t++) {
        double result = a(t);
        fprintf(fp, "%d %lf\n", t, result);
    }
    
    fclose(fp);
    return 0;
}

