#include<stdio.h>
int main(){
    int n ;
    printf("Enter The Number = ");
    scanf("%d",&n);
    char a = 'A';
    for(int i = 1 ; i<=n;i++){
        for(int j= 0; j<i;j++){
            printf("%c",a+j);
        }
        printf("\n");
    }
}