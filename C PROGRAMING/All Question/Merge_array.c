#include <stdio.h>

int main() {
    int arr1[3], arr2[3], merged[6], i, j;

    printf("Enter 3 elements for array 1:\n");
    for (i = 0; i < 3; i++) {
        scanf("%d", &arr1[i]);
    }

    printf("Enter 3 elements for array 2:\n");
    for (i = 0; i < 3; i++) {
        scanf("%d", &arr2[i]);
    }

    for (i = 0; i < 3; i++) {
        merged[i] = arr1[i];
    }

    for (i = 0, j = 3; j < 6; i++, j++) {
        merged[j] = arr2[i];
    }

    printf("Merged array:\n");
    for (i = 0; i < 6; i++) {
        printf("%d ", merged[i]);
    }
    printf("\n");

    return 0;
}