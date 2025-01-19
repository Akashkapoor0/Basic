#include <stdio.h>

int main() {
    FILE *file;
    file = fopen("example.txt", "w");
    if (file == NULL) {
        printf("File could not be opened.\n");
        return 1;
    }
    fprintf(file, "Hello, this is a test file.\n");
    fclose(file);
    printf("File written successfully.\n");

    return 0;
}