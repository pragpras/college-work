#include<stdio.h>
enum months
{
    jan=1,feb,mar=5,apr,may=10,jun,july
};
int main()
{
    enum months m;
    printf("size of m is %lu\n",sizeof(m));
    printf("%d %d %d %d %d %d %d",jan,feb,mar,apr,may,jun,july);
    return 0;
}