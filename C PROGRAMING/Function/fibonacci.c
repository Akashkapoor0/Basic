#include <stdio.h>

void fibonacci(int n) {
    if (n == 0)
        return;
    else if (n == 1)
        printf("0 ");
    else if (n == 2)
        printf("0 1 ");
    else {
        int a = 0, b = 1, next;
        printf("0 1 ");
        for (int i = 3; i <= n; i++) {
            next = a + b;
            printf("%d ", next);
            a = b;
            b = next;
        }
    }
}

int main() {
    int n;
    printf("Enter the number : ");
    scanf("%d", &n);
    
    fibonacci(n);
    return 0;
}
