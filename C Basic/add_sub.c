#include<stdio.h>
int main(){
    int n;
    printf("Ente the number = ");
    scanf("%d",&n);
    int count = 1;
    int sum = 0;
    for(int i = 1 ; i<=n;i++){
        if(count%2==0||count == 1){
            sum = sum +i;
        }
        else{
            sum = sum -i;
        }
        count++;
    }
    printf("%d",sum);
}