#include <stdio.h>

int main() {
    int arr[5], i, isSorted = 1;

    printf("Enter 5 elements:\n");
    for (i = 0; i < 5; i++) {
        scanf("%d", &arr[i]);
    }

    for (i = 0; i < 4; i++) {
        if (arr[i] > arr[i + 1]) {
            isSorted = 0;
            break;
        }
    }

    if (isSorted) {
        printf("The array is sorted in ascending order.\n");
    } else {
        printf("The array is not sorted.\n");
    }

    return 0;
}