#include<stdio.h>
int hcf(int a, int b) {
    if (b == 0)
        return a;
    else
        return hcf(b, a % b);
}
int main(){
    int a, b;
    printf("Enter the numbers: ");
    scanf("%d %d", &a, &b);
    printf("HCF: %d\n", hcf(a, b));
    return 0;
}
