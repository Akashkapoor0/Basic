#include <stdio.h>

void updateValue(int num) {
    num = num + 10;
}

int main() {
    int value = 5;
    updateValue(value);
    printf("%d\n", value);
    return 0;
}