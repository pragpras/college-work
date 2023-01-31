#include<stdio.h>
void main()
{
    int a=10;
    int *ptr=&a;
    printf("Value of variable:%d\n",*ptr);
    printf("Address of variable:%p\n",ptr);
    *ptr=20;
    printf("After doing *ptr=20, *ptr is now %d\n",*ptr);
}