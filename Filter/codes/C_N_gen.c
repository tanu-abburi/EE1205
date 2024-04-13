#include <stdio.h>
#include <math.h>

#define N 4

int main() {
    double Omega_L, x, c_N;
    FILE *file;

    file = fopen("cn_values.txt", "w");
    if (file == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    for (Omega_L = 0; Omega_L <= 2.0; Omega_L += 0.01) {
        x = Omega_L / 1.0; // Assuming Omega_Lp is 1
        if (x <= 1) {
            c_N = cos(N * acos(x));
        } else {
            c_N = cosh(N * acosh(x));
        }
        fprintf(file, "%.2f %.8f\n", Omega_L, c_N);
    }

    fclose(file);
    printf("Values of C_N written to cn_values.txt\n");

    return 0;
}
