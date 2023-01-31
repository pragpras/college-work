//gives binary value of the given number
#include<stdio.h>
int what1(int n)
{
    if(n==0)
    return 0;
    else
    return (n%2)+10*(what1(n/2));
}
int main()
{
    printf("%d",what1(10));
    return 0;
}