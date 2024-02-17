#include <stdio.h>
#include <math.h>

int main() {
    FILE *file;
    file = fopen("values.dat", "w");

    if (file == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    double t, a;
    for (t = 0; t <= 15; t++) {
        a = (-0.25 * pow(t, 2) + 10 * t + 10) / 10;
        fprintf(file, "%.2f\n", a);
    }

    fclose(file);
    printf("Values written to values.dat.\n");
    return 0;
}

