#include <stdio.h>

float fact(int a) {
    float fac = 1;
    float num = 0;
    for (int i = 1; i <= a; i++) {
        fac *= i;
        num += (float)i / fac;
    }
    return num;
}

int main() {
    int n;
    printf("Enter The Number: ");
    scanf("%d", &n);
    printf("Sum of the series: %f\n", fact(n));
    return 0;
}