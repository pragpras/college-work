#include<stdio.h>
#include<stdlib.h>
int main()
{
    int *p=(int*)calloc(5,sizeof(int));
    *p=10;
    printf("%d\n",*p);
    *(p+3)=30;
    printf("%d\n",*p);
    p=(int*)realloc(p,8*sizeof(int));
    p=p+3;
    printf("%d\n",*p);
    p=p+4;
    printf("%d\n",*(p-1));
    return 0;
}