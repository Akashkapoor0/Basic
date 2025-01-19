#include <stdio.h>

int main() {
    int arr[5], i, smallest;

    printf("Enter 5 elements:\n");
    for (i = 0; i < 5; i++) {
        scanf("%d", &arr[i]);
    }

    smallest = arr[0];
    for (i = 1; i < 5; i++) {
        if (arr[i] < smallest) {
            smallest = arr[i];
        }
    }

    printf("The smallest element is %d\n", smallest);
    return 0;
}