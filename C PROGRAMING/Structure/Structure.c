#include <stdio.h>

struct Person {
    char name[50];
    int age;
    float height;
};

int main() {
    struct Person p1;

    printf("Enter name: ");
    fgets(p1.name, sizeof(p1.name), stdin);
    printf("Enter age: ");
    scanf("%d", &p1.age);
    printf("Enter height: ");
    scanf("%f", &p1.height);

    printf("\nName: %sAge: %d\nHeight: %.2f\n", p1.name, p1.age, p1.height);

    return 0;
}