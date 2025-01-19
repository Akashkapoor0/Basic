#include <stdio.h>

void printString(char str[]) {
    printf("String: %s\n", str);
}

int main() {
    char name[] = "John";
    printString(name);
    return 0;
}