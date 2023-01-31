#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define NUM 4

struct item
{
    char brand[20];
    char id[10];
    float in_price;
    float out_price;
    int storage;
};

struct item_node
{
    struct item wanted;
    int amount;
    struct item_node *next;
};

int menu();
void establish();
void display_all();
void shop_cart();
int cart_menu();
void add();
void display();
void calculate();

struct item goods[NUM];
struct item_node *cart;

void main()
{
    char yn;
    int star;
    printf("\t\t\t*************************************\n");
    printf("\t\tWelcome to the Grocery Store Management System\n");
    printf("\t\t\t*************************************\n");
    while (1)
    {
        switch (menu())
        {
        case 1:
            establish();
            break;
        case 2:
            display_all();
            break;
        case 3:
            shop_cart();
            break;
        case 4:
            calculate();
            break;
        case 5:
            printf("Do you want to take a minute to give the store a feedback? (Y/N)\n");
            scanf("%c",&yn);
            if(yn=='Y' || yn=='y')
            {
                printf("\nRate the system out of 5, 1 being the lowest and 5 the highest:\n");
                scanf("%d",&star);
                if(star>=4)
                    printf("Thank you for the great feedback! Please visit again!\n");
                else
                    printf("We hope to make your shopping experience better next time.\nPlease consider visiting again!\n");
            }
            else
                continue;
            printf("\nThank you for using this system.\nHave a good day/night!\n");
            exit(0);
        }
    }
}

int menu()
{
    char str[5];
    int select;
    printf("\n\nPlease select the number to operate \n");
    printf("1. Establish inventory information \n");
    printf("2. Display all information \n");
    printf("3. The shopping cart \n");
    printf("4. Payment \n");
    printf("5. Exit \n");
    printf(" Please select the corresponding number 1-5\n");
    while (1)
    {
        fflush(stdin);
        gets(str);
        select = atoi(str);
        if (select < 1 || select > 5)
            printf("Input error, please retype: ");
        else
            break;
    }
    return select;
}

void display_all()
{
    int i;
    FILE *fp;
    fp = fopen("goods", "r");
    for (i = 0; (fread(goods + i, sizeof(struct item), 1, fp)) != 0; i++)
    {
        printf("----------------------------------------\n");
        printf(" Sl.no.   Name        Unit price        Inventory \n");
        printf(" %s       %7s      %7.2f       %8d\n", goods[i].id, goods[i].brand, goods[i].out_price, goods[i].storage);
    }
    fclose(fp);
}

void shop_cart()
{
    while (1)
    {
        switch (cart_menu())
        {
        case 1:
            display();
            break;
        case 2:
            add();
            break;
        case 3:
            return;
        }
    }
}

int cart_menu()
{
    char str[5];
    int select;
    printf("\n Please select operation \n");
    printf("----------------------------------------\n");
    printf("1. Display the current shopping list \n");
    printf("2. Add the goods \n");
    printf("3. Exit \n");
    printf("--------------------------------------\n\n");
    while (1)
    {
        fflush(stdin);
        gets(str);
        select = atoi(str);
        if (select < 1 || select > 3)
            printf("Input error, please retype: ");
        else
            break;
    }
    return select;
}

void display()
{
    struct item_node *p = cart;
    if (p == NULL)
    {
        printf("Empty shopping cart \n");
        return;
    }
    while (p != NULL)
    {
        printf("----------------------------------------\n");
        printf(" Sl.no.   Name        Unit price        Inventory \n");
        printf(" %s       %7s      %7.2f       %8d\n", p->wanted.id, p->wanted.brand, p->wanted.out_price, p->amount);
        p = p->next;
    }
}

void add()
{
    FILE *fp;
    int i, n;
    char str[20];
    char choice1, choice2;
    struct item_node *p, *p1;
    do
    {
        printf("Enter the name or article number of the item you want : ");
        fflush(stdin);
        gets(str);
        if ((fp = fopen("goods", "r")) == NULL)
        {
            printf("Failed to open file :(\n");
            continue;
        }
        for (i = 0; fread(goods + i, sizeof(struct item), 1, fp) != 0; i++)
        {
            if ((strcmp(goods[i].brand, str) == 0 || strcmp(goods[i].id, str) == 0) && goods[i].storage != 0)
            {
                printf("The necessary items have been found : \n");
                printf("----------------------------------------\n");
                printf(" Sl.no.   Name        Unit price        Inventory \n");
                printf(" %s       %7s      %7.2f       %8d\n", goods[i].id, goods[i].brand, goods[i].out_price, goods[i].storage);
                printf("Please enter the required quantity : ");
                scanf("%d", &n);
                if (n > goods[i].storage)
                {
                    printf("Insufficient inventory \n");
                    break;
                }
                printf("\nConfirm purchase? (Y/N)\n");
                fflush(stdin);
                choice1 = getchar();
                if (choice1 == 'Y' || choice1 == 'y')
                {
                    p1 = (struct item_node *)malloc(sizeof(struct item_node));
                    if (p1 == NULL)
                    {
                        printf("Memory request failed!\n");
                        exit(1);
                    }
                    p1->amount = n;
                    p1->wanted = goods[i];
                    p1->next = NULL;
                    p = cart;
                    if (cart == NULL)
                        cart = p1;
                    else
                    {
                        while (p->next != NULL)
                            p = p->next;
                        p1->next = p->next;
                        p->next = p1;
                    }
                }
                break;
            }
        }
        if (i == NUM)
            printf("No required items were found :(\n");
        fclose(fp);
        printf("Continue shopping? (Y/N)\n");
        fflush(stdin);
        choice2 = getchar();
    } while (choice2 == 'Y' || choice2 == 'y');
}

void establish()
{
    FILE *fp;
    int i;
    printf("Please enter the cargo information in turn :\n");
    printf("----------------------------------------\n");
    for (i = 0; i < NUM; i++)
    {
        printf("Name : ");
        fflush(stdin);
        gets(goods[i].brand);
        printf("Sl.no : ");
        fflush(stdin);
        gets(goods[i].id);
        printf("Cost price : ");
        fflush(stdin);
        scanf("%f", &goods[i].in_price);
        printf("Selling price : ");
        fflush(stdin);
        scanf("%f", &goods[i].out_price);
        printf("Quantity : ");
        fflush(stdin);
        scanf("%d", &goods[i].storage);
        printf("\n");
    }
    if ((fp = fopen("goods", "w")) == NULL)
    {
        printf("File creation failed :(\n");
        return;
    }
    fwrite(goods, sizeof(struct item), NUM, fp);
    fclose(fp);
}

void calculate()
{
    float total = 0, pay;
    struct item_node *p;
    int i;
    FILE *fp;
    printf("Here is the shopping list : \n");
    display();
    if ((fp = fopen("goods", "r")) == NULL)
    {
        printf("Failed to open file :(\n");
        return;
    }
    for (i = 0; (fread(goods + i, sizeof(struct item), 1, fp)) != 0; i++)
        ;
    fclose(fp);
    p = cart;
    while (p != NULL)
    {
        total += p->wanted.out_price * p->amount;
        for (i = 0; strcmp(goods[i].id, p->wanted.id) != 0; i++)
            ;
        goods[i].storage -= p->amount;
        p = p->next;
    }
    if(total>=500 && total<1000)
    {
        printf("You can avail a discount of 5 percent on your total bill\n",total);
        total=total-(0.05*total);
    }
    else if(total>=1000 && total<2000)
    {
        printf("You can avail a discount of 10 percent on your total bill\n",total);
        total=total-(0.10*total);
    }
    else if(total>=2000)
    {
        printf("You can avail a discount of 20 percent on your total bill\n",total);
          total=total-(0.20*total);
    }
    printf("The discounted total is %7.2f", total);
    printf("\nEnter the actual amount paid: \n");
    scanf("%f",&pay);
    printf("Amount paid:   %7.2f \nChange:   %7.2f", pay, pay - total);
    if ((fp = fopen("goods", "w")) == NULL)
    {
        printf("Failed to open file :(\n");
        return;
    }
    fwrite(goods, sizeof(struct item), NUM, fp);
    fclose(fp);
} 