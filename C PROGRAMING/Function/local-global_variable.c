#include <stdio.h>

int globalVar = 100;

void display() {
    int localVar = 50;
    printf("Global Variable: %d\n", globalVar);
    printf("Local Variable: %d\n", localVar);
}

int main() {
    display();
    return 0;
}