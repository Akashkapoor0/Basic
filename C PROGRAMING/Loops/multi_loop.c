#include <stdio.h>

int main() {
    int i, j;
    for (i = 1, j = 5; i <= 5; i++, j--) {
        printf("i = %d, j = %d\n", i, j);
    }
    return 0;
}