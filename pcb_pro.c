#include<stdio.h>
#include<stdlib.h>

typedef struct pcb
{
    int id;
    char state;
    int total_time;
    int cputime;
    int priority;
}*proc;

int proc_num;
proc head;
int init_pcb();
void display();
void sort();
void priority_queue();




int main()
{
    init_pcb();
    printf("\nInited pcb\n\n");
    display();
    printf("\nDisplayed\n\n");
    sort(head);
    printf("\nSorted\n\n");
    priority_queue();
    printf("\nOver\n\n");

    return 0;
}





int init_pcb()
{
    int i=0;
    proc p;
    printf("please input the number of processes:\n");
    scanf("%d",&proc_num);
    printf("there are %d processes, please input pcb info:\n",proc_num);

    p = (proc)malloc(sizeof(struct pcb) * proc_num);
    head = p;

    for(i = 0; i<proc_num; i++)
    {
        printf("process id:");
        scanf("%d",&p->id);
        printf("cpu time required:");
        scanf("%d",&p->total_time);
        printf("priority:");
        scanf("%d",&p->priority);
        p->state = 'R';
        p->cputime = 0;
        p++;
    }

    return 0;
}

void display()
{
    int i;
    proc p = head;
    printf("pid\tcpu_time\treq_time\tpriority\n");
    for(i=0; i<proc_num; i++)
    {
        printf("%d\t%d\t%d\t%d\n",p->id,p->cputime,p->total_time,p->priority );
        p++;
    }
}

void priority_queue()
{
    int round = 1;
    proc p = head;
    while(proc_num) //����PCB
    {

        while(p->state == 'R')
        {
            printf("\nRound %d, Process %d is running \n",round, p->id);
            p->cputime ++;
            display();
            if(p->cputime == p->total_time)
            {
                p->state = 'E';
                proc_num --;
            }
            round++;
        }
        p++;


    }
}
void sort(proc arr)
{
    int i,j,temp;
    for ( i = 0; i<proc_num - 1; i++)
        for (j = 0; j <proc_num - i - 1; j++)
        {
            //���ǰ������Ⱥ���󣬽��н���
            if (arr[j].priority > arr[j + 1].priority)
            {
                temp = arr[j].priority;
                arr[j].priority = arr[j + 1].priority;
                arr[j + 1].priority = temp;
                temp = arr[j].id;
                arr[j].id = arr[j + 1].id;
                arr[j + 1].id = temp;
            }
        }
}

