#include<stdio.h>
int main(){
    printf("Enter a number: ");
    int a;
    scanf("%d",&a);
    int b;
    int add = 0;
    while(a>0){
        b = a%10;
        add += b;
        a = a/10;
    }
    printf("The sum of digits is: %d",add);
}