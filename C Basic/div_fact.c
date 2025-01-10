#include <stdio.h>
unsigned long long factorial(int n) {
    if (n == 0 || n == 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

int main() {
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    float v = 0;
    for (int i = 1; i <= n; i++) {
        printf("%d/%d! = %.10f\n", i, i, (double)i / factorial(i));
        v += ((double)i / factorial(i));
    }
    printf("sum is %f",v);
    return 0;
}