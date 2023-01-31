#include<stdio.h>
#include<string.h>
union car
{
    char name[10];
    float price;
};
int main()
{
    union car c;
    strcpy(c.name,"Benz");
    printf("%s\n",c.name);
    c.price=40000.00;
    printf("%f",c.price);
    return 0;
}