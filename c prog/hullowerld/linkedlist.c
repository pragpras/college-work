/*implementation of ordered list:
algo to be followed:
-create an empty list and initialize the list to NULL
-as and when the user enters element, make a node
-insert this node to the list based on the order of the elements of the node
-cases to considered 

pictorial representations:
-initializing the list*/

#include<stdio.h>
struct node
{
    int info;
    struct node *link;
};
typedef struct node node_t;
struct mylist
{
    node_t *head;
};
#include<stdlib.h>
typedef struct mylist mylist_t;
void initialize_list(mylist_t*);
void insert_list(mylist_t*,int);
void free_list(mylist_t*);
void display(const mylist_t*);
int main()
{
    mylist_t my_list;
    initialize_list(&my_list);
    int n,i,ele;
    printf("enter the number of elements you want to insert to list");
    return 0;
}
void initialize_list(my_list* p_list)
{
    p_list->head=NULL;
}
void insert_list(my_list* p_list,int e)
{
    node_t* temp=(node_t)* malloc(sizeof(node_t));
    temp->info=e;
    temp->link=NULL;
    if(p_list->head==NULL)
        p_list->head=temp;
    else
    {
        node_t *present=p_list->head;
        node_t *prev=NULL;
        while(present!=NULL && present->info<e)
        {
            prev=present;
            present=present->link;
        }
        if(prev==NULL)
        {
            temp->link=present;
            p_list->head=temp;
        }
        else
        {
            temp->link=present;
            prev->link=temp;
        }
    }
}
void free_list(mylist_t* p_list)
{

}
void display(const mylist_t* p_list)
{
    node_t *p=p_list->head;
    if(p==NULL)
        printf("no node is available in the list to free it\n");
    else
    {
        while()
    }
}

