#include <stdio.h>
#include <math.h>

// Function to calculate activity of the catalyst
double activity(double t) {
    return (-0.25 * pow(t, 2) + 10 * t + 10) / 10;
}

int main() {
    FILE *fp;
    fp = fopen("values.dat", "w");
    
    if (fp == NULL) {
        printf("Error opening file.\n");
        return -1;
    }
    
    // Generate time values from 0 to 10 hours
    for (double t = 0; t <= 10; t += 0.1) {
        // Calculate activity
        double a = activity(t);
        // Write time and activity to file
        fprintf(fp, "%.2f %.2f\n", t, a);
    }
    
    fclose(fp);
    
    return 0;
}

