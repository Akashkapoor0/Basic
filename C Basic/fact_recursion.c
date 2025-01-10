#include<stdio.h>
int fact(int a){
    if(a==1){
        return 1;
    }
    else{
        return (fact(a)*fact(a-1));
        }
}
int main(){
    int a;
    scanf("%d",&a);
    printf("%d",fact(a));
}