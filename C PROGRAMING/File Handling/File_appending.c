#include <stdio.h>

int main() {
    FILE *file;
    file = fopen("example.txt", "a");
    if (file == NULL) {
        return 1;
    }

    fprintf(file, "Appending new text to the file.\n");
    fclose(file);

    printf("File appended successfully.\n");
    return 0;
}