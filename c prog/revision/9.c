#include <stdio.h>
int main()
{
    register int i=0;
    int *a;
    a=&i;
    printf("%d",a);
    getchar();
    return 0;
}