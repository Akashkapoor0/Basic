#include<stdio.h>
int main(){
    int a;
    scanf("%d",&a);
    for(int i = a ; i >=1;i--){
        for(int j = 1; j <=i-1; j++){
            printf(" ");
        }
        for(int j = i ; j>=1;j--){
            printf("*");
        }
        printf("\n");
    }
}