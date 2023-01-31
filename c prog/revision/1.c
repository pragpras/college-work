#include<stdio.h>
int main()
{
    int i,r;
    i=4;
    r=++i+i++;
    printf("%d\n",r);
    return 0;
}
//expected o/p is 10 but it gives us 11 due to undefined behaviour of c lang