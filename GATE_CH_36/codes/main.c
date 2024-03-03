#include <stdio.h>
#include <math.h>

double y(double t) {
    return 6 - 11.0/26 * exp(-t) + 5.0/26 * exp(-2*t) + 5.0/78 * exp(-3*t);
}

int main() {
    FILE *fp;
    double t, result;
    
    fp = fopen("values.dat", "w");
    if (fp == NULL) {
        printf("Error opening file.\n");
        return 1;
    }
    
    // Evaluate y(t) for t values from 0 to 5
    for (t = 0; t <= 5; t += 0.1) {
        result = y(t);
        fprintf(fp, "%lf %lf\n", t, result);
    }
    
    // Calculate and print the value at t = infinity
    result = y(INFINITY);
    fprintf(fp, "Infinity %lf\n", result);
    
    fclose(fp);
    printf("Values written to values.dat\n"); // Print a message indicating completion
    
    return 0;
}

