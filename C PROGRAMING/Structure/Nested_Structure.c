#include <stdio.h>

struct Address {
    char street[100];
    char city[50];
    char zip[10];
};

struct Person {
    char name[50];
    struct Address address;
};

int main() {
    struct Person p1;

    printf("Enter name: ");
    fgets(p1.name, sizeof(p1.name), stdin);
    printf("Enter street: ");
    fgets(p1.address.street, sizeof(p1.address.street), stdin);
    printf("Enter city: ");
    fgets(p1.address.city, sizeof(p1.address.city), stdin);
    printf("Enter zip code: ");
    fgets(p1.address.zip, sizeof(p1.address.zip), stdin);

    printf("\nName: %sAddress: %s%s%s", p1.name, p1.address.street, p1.address.city, p1.address.zip);

    return 0;
}