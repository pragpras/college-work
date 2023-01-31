#include<stdio.h>
void swap1(int, int);
void swap2(int *,int *);
int main()
{
    int a=5,b=6;
    printf("%d %d\n",a,b);
    swap1(a,b);
    printf("%d %d\n",a,b);
    swap2(&a,&b);
    printf("%d %d\n",a,b);
    return 0;
}
void swap1(int a,int b)
{
    int temp=a;
    a=b;
    b=temp;
}
void swap2(int *x,int *y)
{
    int temp=*x;
    *x=*y;
    *y=temp;
}
/*output
5 6
5 6
6 5*/