#include <stdio.h>

int main() {
    FILE *file;
    file = fopen("values.txt", "w");

    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    for (int n = 1; n <= 10; ++n) {
        int x_n = 5 + 3 * n;
        fprintf(file, "%d\n", x_n);
    }

    fclose(file);

    return 0;
}

