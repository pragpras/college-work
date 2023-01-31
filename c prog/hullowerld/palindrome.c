// check if a given number is a palindrome or not
#include<stdio.h>
void main()
{
    int d,n;
    printf("Enter a number: ");
    scanf("%d",&d);
    int rev=0;
    int og=d;
    while (d!=0)
    {
        n=d%10;
        rev=rev*10+n;
        d=d/10;
    }
    printf("%d",rev);
    if (rev==og)
        printf("The number is a palindrome");
    else
        printf("The number is not a palindrome");
}