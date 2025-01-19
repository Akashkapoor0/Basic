#include <stdio.h>

void rotate(int arr[], int n, int k) {
    int temp[k], i, j;

    for (i = 0; i < k; i++) {
        temp[i] = arr[n - k + i];
    }

    for (i = n - 1; i >= k; i--) {
        arr[i] = arr[i - k];
    }

    for (i = 0; i < k; i++) {
        arr[i] = temp[i];
    }
}

int main() {
    int arr[5], i, k;

    printf("Enter 5 elements:\n");
    for (i = 0; i < 5; i++) {
        scanf("%d", &arr[i]);
    }

    printf("Enter the number of positions to rotate: ");
    scanf("%d", &k);

    rotate(arr, 5, k);

    printf("Array after rotation:\n");
    for (i = 0; i < 5; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}