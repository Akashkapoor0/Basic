#include <stdio.h>

int main() {
    FILE *file;
    char str[100];

    file = fopen("example.txt", "w");
    if (file == NULL) {
        printf("File could not be opened.\n");
        return 1;
    }

    printf("Enter a string to write to file: ");
    fgets(str, sizeof(str), stdin);
    fputs(str, file);

    fclose(file);
    printf("String written to file successfully.\n");

    return 0;
}