#include <stdio.h>

int main() {
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);
    
    if (num > 0) {
        printf("The number is positive.\n");
    }
    return 0;
}