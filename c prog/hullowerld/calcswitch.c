// to make a simple calculator using switch statements
#include<stdio.h>
void main()
{
    printf("Enter the operation you want to perform: +,-,*,/");
    char c;
    scanf("%c",&c);
    int a,b;
    printf("Enter the operands: ");
    scanf("%d%d",&a,&b);
    switch (c)
    {
    case '+':
        printf("%d",a+b);
        break;
    case '-':
        printf("%d",a-b);
        break;
    case '*':
        printf("%d",a*b);
        break;
    case '/':
        printf("%d",a/b);
        break;    
    default:
        break;
    }
}