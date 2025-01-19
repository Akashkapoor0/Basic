#include <stdio.h>

int main() {
    char names[3][20] = {"Alice", "Bob", "Charlie"};

    for (int i = 0; i < 3; i++) {
        printf("Name %d: %s\n", i+1, names[i]);
    }

    return 0;
}