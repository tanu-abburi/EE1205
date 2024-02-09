#include <stdio.h>

#define START_N -4
#define END_N 10 // Number of values from -4 to 10

int main() {
    FILE *fp;
    fp = fopen("values.dat", "w");
    
    if (fp == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    // Generating x(n) = 5 + 3n * u(n)
    for (int n = START_N; n <= END_N; n++) {
        int x_n = n >= 0 ? 5 + 3 * n : 0;
        fprintf(fp, "%d\n", x_n);
    }
    
    fclose(fp);
    printf("Values written to values.dat\n");

    return 0;
}

