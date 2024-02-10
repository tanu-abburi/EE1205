#include <stdio.h>

int main() {
    FILE *file;
    file = fopen("values.dat", "w");

    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    int n;
    for (n = -4; n <= 10; n++) {
        if (n >= 0) {
            fprintf(file, "%d\n", 1 + 2 * n);
        } else {
            fprintf(file, "0\n");
        }
    }

    fclose(file);
    return 0;
}

