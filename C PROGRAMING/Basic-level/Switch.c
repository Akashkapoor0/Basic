#include <stdio.h>

int main() {
    int num;
    printf("Enter a number (1-3): ");
    scanf("%d", &num);
    
    switch (num) {
        case 1:
            printf("You selected one.\n");
            break;
        case 2:
            printf("You selected two.\n");
            break;
        case 3:
            printf("You selected three.\n");
            break;
        default:
            printf("Invalid choice.\n");
    }
    return 0;
}