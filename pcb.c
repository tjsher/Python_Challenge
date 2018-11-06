#include<stdio.h>
#include<stdlib.h>

typedef struct pcb
{
  int id;
  char state;
  int total_time;
  int cputime;
  struct pcb* next;
}*proc;

int proc_num;
proc head,tail;
int init_pcb();
void display();
void sched();

int init_pcb()
{
  int i=0;
  proc p,temp;
  printf("please input the number of processes:\n");
  scanf("%d",&proc_num);
  printf("there are %d processes, please input pcb info:\n",proc_num);

  p = (proc)malloc(sizeof(struct pcb));
  printf("process id:");
  scanf("%d",&p->id);
  printf("cputime required:");
  scanf("%d",&p->total_time);
  p->state = 'R';
  p->cputime = 0;
  head = p;
  for(i = proc_num;i>1;i--){
    tmp = p;
    p = (proc)malloc(sizeof(struct pcb));
    printf("process id:");
    scanf("%d",&p->id);
    printf("cputime required:");
    scanf("%d",&p->total_time);
    p->state = 'R';
    p->cputime = 0;
    temp->next=p;
  }
  tail = p;
  p->next = head;
  return 0;
}

void display()
{
  int i;
  proc p = head;
  printf("pid\tcpu_time\treq_time\n");
  for(i=0;i<proc_num;i++)
  {
    printf("%d\t%d\t%d\n",p->id,p->cputime,p->total_time );
    p = p->next;
  }
}

void sched()
{
  int round = 1;
  proc temp = tail;
  proc p = head;
  while(p->total_time > p->cputime)
  {
    printf("\nRound %d, Process %d is running \n",round, p->id);
    p->cputime ++;
    display();
    if(p->total_time == p-> cputime)
    {
      p->state = 'E';
      proc_num --;
      temp->next = p->next;
      if(p == head) head = p->next;
      printf("process %d is finished\n",p->id);
    }
    else
    temp = p;
    p = p->next;
    round++;
  }
}


void main(){
  init_pcb();
  display();
  sched();
  display();
}
