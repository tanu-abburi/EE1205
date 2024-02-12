#include <stdio.h>

int main() {
    FILE *fp;
    fp = fopen("values.dat", "w");
    if (fp == NULL) {
        printf("Error opening file.\n");
        return 1;
    }
    
    int n;
    for (n = -4; n <= 10; n++) {
        fprintf(fp, "%d\n", n);
    }

    fclose(fp);
    return 0;
}

