/* 
- a line or sequence of people or vehicles awaiting for their turn to be attented or to proceed
- in comp science a list of data items, commands etc stored so as to be retrievable in a definite order
- a data structure which has 2 ends- rear end and a front end (open ended at both ends)
- data elements are inserted into the queue from the rear end and deleted from the front end
- follows the principle of first in first out (FIFO)
operations on queue:
- enqueue: add (store) an item to the queue from the rear end
- dequeue: 
types of queues:
- ordinary queue: insertion takes place at the rear end and deletion takes place at the front end
- priority queue: special type of queue in which each element is associated with a priority and is served according to its priority. if elements with the same priority occur, they are served according ot their order in the queue.
- circular queue: last element points to the first element of queue making circular link
- double ended queue: insertion and removal of elements can be performed at both front and rear ends

priority queue:
- type of queue where each element has a "priority" associated with it
- priority decides about the deque operation
- the enque operation stores the item and the "priority" information

applications of priority queue:
- implementation of heap data structure
- dijkstra's shortest path algorithm
- prim's algorithm

implementation of priority queue:
- using an unordered array
- using an ordered array
- using an unordered linked list
- using an ordered linked list
- using heap

- balls in your mom every night 
- cum in your mom every night
- peepee in your mom every night
- weewee in your mom every night
- penibs in your mom every night
- dingalong in your mom every night
- big willie in your mom every night

implementation of priority queue
- using an unordered linked list
    - involves defining new variables
*/

#include<stdio.h>
#include<stdlib.h>
struct queue{
    int data;
    int priority;
    struct queue *next;
};

struct queue *front=NULL;

void insert(){
    struct queue *temp, *q;
    temp = (struct queue*) malloc(sizeof(struct queue));
    printf("Enter date and priority:\n");
    scanf("%d %d",&(temp->data),&(temp->priority));
    if(front==NULL || temp->priority<front->priority){
        temp->next=front;
        front=temp;
    }
    else{
        q=front;
    }
    while(q->next!=NULL && q->next->priority<=temp->priority){
        q=q->next;
    
    }
};


int main(){
    int option;
    while(1){
        printf("1: INSERT\n");
        printf("2: DELETE\n");
        printf("3: DISPLAY\n");
        printf("4: EXIT\n");
        scanf("%d",&option);
        switch(option){
            case 1: insert();
            break;
            case 2: delete();
            break;
            case 3: display();
            break;
            case 4: return 0;
            default: printf("Invalid option");
        }


    }
    return 0;
}