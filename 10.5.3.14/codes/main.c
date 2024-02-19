#include <stdio.h>

int main() {
    FILE *fp;
    fp = fopen("value.dat", "w");
    if (fp == NULL) {
        printf("Error opening file.\n");
        return 1;
    }
    
    int n;
    for (n = -4; n <= 25; n++) {
        fprintf(fp, "%d\n", n);
    }

    fclose(fp);
    return 0;
}


