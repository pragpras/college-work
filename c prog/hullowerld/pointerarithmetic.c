//to demonstrate pointer arithmetic using an array
#include<stdio.h>
int main()
{
    int v[3]={10,100,1000};
    int *ptr;
    ptr=v; //assigns the address of v[0] to ptr
    for (int i=0;i<3;i++)
    {
        printf("Value of *ptr=%d\n",*ptr);
        printf("Value of ptr=%p\n",ptr);
        ptr++;
    }
    return 0;
}