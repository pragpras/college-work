#include<stdio.h>
int main()
{
    int a[][2]={34,55,11,17,20,60};
    printf("%d",*(*a+5));
    return 0;
}