#include<stdio.h>
#include<math.h>
int main(){
    int n;
    int a;
    printf("Enter The Number and time : ");
    scanf("%d%d",&n,&a);
    int total = 0;
    int num;
    for(int i = 1; i<=a;i++){
        num = pow(n,i);
        printf("%d ",num);
        if(i != a){
            printf(" + ");
        }
        else{
            printf("=");
        }
        total += num;
    }
    printf(" %d",total);
}