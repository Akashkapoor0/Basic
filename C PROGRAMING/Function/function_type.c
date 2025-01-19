#include <stdio.h>

void printMessage() {
    printf("Hello from a void function\n");
}

int multiply(int a, int b) {
    return a * b;
}

int main() {
    printMessage();
    int result = multiply(4, 5);
    printf("%d\n", result);
    return 0;
}