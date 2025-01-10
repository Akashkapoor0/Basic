#include<stdio.h>
long int power(int a,int b){
    if(b == 1){
        return a;
    }
    else{
        return a*power(a,b-1);
    }
}
int main(){
    int a,b;
    printf("Enter base: ");
    scanf("%d", &a);
    printf("Enter exponent: ");
    scanf("%d", &b);
    printf("Result: %ld\n", power(a, b));
    return 0;
}