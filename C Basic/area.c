#include<stdio.h>
int main(){
    int n;
    int a,b;
    printf("For Rectangle Press 1\n");
    printf("For Circle Press 2\n");
    printf("For Square Press 3\n");
    printf("For Triangle Press 4\n");
    scanf("%d",&n);
    switch (n){
        case 1 : printf("Enter the Length = ");
        scanf("%d",&a);
        printf("Enter the Height = ");
        scanf("%d",&b);
        printf("Area of Rectangle is %d",a*b);
        break;

        case 2 : printf("Enter the Radius = ");
        scanf("%d",&a);
        printf("Area of Circle is %d",3.14*a*a);
        break;

        case 3 : printf("Enter the Length = ");
        scanf("%d",&a);
        printf("Area of Square is %d",a*a);
        break;

        case 4 : printf("Enter the Length = ");
        scanf("%d",&a);
        printf("Enter the Height = ");
        scanf("%d",&b);
        printf("Area of Triangle is %d",(1/2*a*b));
        break;
        
    }
}