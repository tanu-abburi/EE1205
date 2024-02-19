#include <stdio.h>

// Function for convolution
void convolution(const int *array1, int len1, const int *array2, int len2, int *result) {
    int lenResult = len1 + len2 - 1;
    for (int i = 0; i < lenResult; i++) {
        result[i] = 0;
    }
    for (int i = 0; i < len1; i++) {
        for (int j = 0; j < len2; j++) {
            result[i + j] += array1[i] * array2[j];
        }
    }
}

// Function for calculating sum of an arithmetic progression
void sum_of_ap(int a, int d, int N) {

    // Generating the AP sequence
    int x[N];
    for (int i = 0; i < N; i++) {
        x[i] = a + i * d;
    }

    // Creating a sequence of 1s
    int u[N];
    for (int i = 0; i < N; i++) {
        u[i] = 1;
    }
 
    // Performing convolution
    int result[N + N - 1];
    convolution(x, N, u, N, result);
    
    // Writing results to a file
    FILE *file = fopen("theory.dat", "w");
    if (file == NULL) {
        printf("Error opening file.\n");
        return;
    }
    for (int i = 0; i < N ; i++) {
        fprintf(file, "%d\n", result[i]);
    }
    fclose(file);
}

int main() {
    // Analysis code
    int a = 1;  // First term of the arithmetic progression
    int d = 2;  // Common difference of the arithmetic progression
    int N = 25; // Number of terms to sum

    // Computing the sum of the first N terms of the AP
    sum_of_ap(a, d, N);

    // Simulation code
    int sum_of_odds = 0;
    FILE *simulatedFile = fopen("simulated.dat", "w");
    if (simulatedFile == NULL) {
        printf("Error opening simulated file.\n");
        return 1;
    }
    for (int num = 1; num <= 50; num++) {
        if (num % 2 != 0) {
            sum_of_odds += num;
            fprintf(simulatedFile, "%d\n", sum_of_odds); // Writing each sum to file
        }
    }
    fclose(simulatedFile);

    return 0;
}

