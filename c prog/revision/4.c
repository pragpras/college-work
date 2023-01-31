#include<stdio.h>
void main()
{
    int a=12;
    for(;;)
    {
    printf("%d",a);
    switch(a)
    {
        case 1: break;
        case 2: break;
        case 12: a=1; break;
    }
    }
}