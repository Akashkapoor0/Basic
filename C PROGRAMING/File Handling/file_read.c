#include <stdio.h>

int main() {
    FILE *file;
    char ch;

    file = fopen("example.txt", "r");
    if (file == NULL) {
        printf("File could not be opened.\n");
        return 1;
    }

    while ((ch = fgetc(file)) != EOF) {
        putchar(ch);
    }

    fclose(file);
    return 0;
}