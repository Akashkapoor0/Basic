#include <stdio.h>

int main() {
    int m, n, p, q, i, j, k;

    printf("Enter rows and columns for matrix 1: ");
    scanf("%d %d", &m, &n);

    int matrix1[m][n];

    printf("Enter elements of matrix 1:\n");
    for (i = 0; i < m; i++) {
        for (j = 0; j < n; j++) {
            scanf("%d", &matrix1[i][j]);
        }
    }

    printf("Enter rows and columns for matrix 2: ");
    scanf("%d %d", &p, &q);

    if (n != p) {
        printf("Matrix multiplication not possible.\n");
        return 0;
    }

    int matrix2[p][q], result[m][q];

    printf("Enter elements of matrix 2:\n");
    for (i = 0; i < p; i++) {
        for (j = 0; j < q; j++) {
            scanf("%d", &matrix2[i][j]);
        }
    }

    for (i = 0; i < m; i++) {
        for (j = 0; j < q; j++) {
            result[i][j] = 0;
            for (k = 0; k < n; k++) {
                result[i][j] += matrix1[i][k] * matrix2[k][j];
            }
        }
    }

    printf("Resultant Matrix:\n");
    for (i = 0; i < m; i++) {
        for (j = 0; j < q; j++) {
            printf("%d ", result[i][j]);
        }
        printf("\n");
    }

    return 0;
}