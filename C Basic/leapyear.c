#include<stdio.h>
int main(){
    int year;
    printf("Enter A Year = ");
    scanf("%d",&year);
    if(year % 400==0){
        printf("Leap Year");
    }
    else if(year %100==0){
        printf("Year is not leap Year");

    }
    else if(year%4 == 0 ){
        printf("Year is leap year");

    }
    else {
        printf("Not leap year");
    }
}