#include <stdio.h>

struct Student {
    char name[50];
    int marks;
};

int main() {
    struct Student students[2];

    for (int i = 0; i < 2; i++) {
        printf("Enter name of student %d: ", i+1);
        fgets(students[i].name, sizeof(students[i].name), stdin);
        printf("Enter marks of student %d: ", i+1);
        scanf("%d", &students[i].marks);
        getchar(); // To consume the newline character left by scanf
    }

    for (int i = 0; i < 2; i++) {
        printf("\nStudent %d: %sMarks: %d\n", i+1, students[i].name, students[i].marks);
    }

    return 0;
}