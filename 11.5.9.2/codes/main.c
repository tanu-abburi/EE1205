#include <stdio.h>

int main() {
    FILE *file;
    file = fopen("values.dat", "w");

    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    for (int n = -5; n <= 10; ++n) { // Start n from 0 and iterate until 9
        int x_n = 5 + 3 * n;
        fprintf(file, "%d\n", x_n);
    }

    fclose(file);

    return 0;
}

