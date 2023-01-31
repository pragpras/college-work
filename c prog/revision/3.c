#include<stdio.h>
#include<string.h>
int main()
{
    char *index;
    int i;
    char a[]="pesu";
    index=strchr(a,'u');
    printf("%p\n",index);
    i=index-a;
    printf("%d",i);
    return 0;
}