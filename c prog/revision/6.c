#include<stdio.h>
int get_what(int n1,int n2);
int main()
{
    int n1=12;
    int n2=10;
    printf("%d",get_what(n1,n2));
    return 0;
}
int get_what(int n1,int n2)
{
    if(n1==0 || n2==0)
        return n2;
    else
        return get_what(n2-2,n1-1);
}