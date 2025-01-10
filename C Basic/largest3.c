#include<stdio.h>
int main(){
    int a,b,c;
    scanf("%d %d %d", &a,&b,&c);
    if(a > b&&a >c){
        printf("A is Greater");
    }
    if(b > a&&b >c){
        printf("B is Greater");
    }
    else{
        printf("C is greater");
    }
}