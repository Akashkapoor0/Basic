#include <stdio.h>
#include <stdlib.h>

int main() {
    int *ptr;
    int n;

    printf("Enter the number of elements: ");
    scanf("%d", &n);

    ptr = (int*) malloc(n * sizeof(int));
    if (ptr == NULL) {
        printf("Memory allocation failed!\n");
        return -1;
    }

    for (int i = 0; i < n; i++) {
        printf("Enter element %d: ", i+1);
        scanf("%d", &ptr[i]);
    }

    printf("\nEntered elements are:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", ptr[i]);
    }

    printf("\nEnter new number of elements: ");
    scanf("%d", &n);

    ptr = (int*) realloc(ptr, n * sizeof(int));
    if (ptr == NULL) {
        printf("Memory reallocation failed!\n");
        return -1;
    }

    for (int i = 0; i < n; i++) {
        printf("Enter element %d: ", i+1);
        scanf("%d", &ptr[i]);
    }

    printf("\nUpdated elements are:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", ptr[i]);
    }

    free(ptr);  
    return 0;
}
