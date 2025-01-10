#include<stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    int a = 0;  
    int b = 1;  

    for (int i = 1; i <= n; i++) {
        printf("%d ", a);  
        int next = a + b;  
        a = b;              
        b = next;           
    }

    return 0;
}
