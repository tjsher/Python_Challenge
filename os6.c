#define TURE 1
#define FALSE 0
#define INVALID -1
#define NULL 0

#define total_instruction 320
#define total_vp 32
#define clear_period 50

#include <stdio.h>
#include <stdlib.h>

typedef struct
{
    int pn,pfn,count,time;
    //pn: page number, pfn: page frame number, count: visited count, time: visited time

} pl_type;
pl_type pl[32];

typedef struct pfc_struct
{
    int pn,pfn;
    //pn: page number, pfn: page frame number

    struct pfc_struct *next;

} pfc_type;
pfc_type pfc[32],*freepf_head,*busypf_head,*busypf_tail;

int diseffect,a[total_instruction];
int page[total_instruction],offset[total_instruction];

void initialize();
void FIFO();
void LRU();
void LFU();
void NUR();

int main(int argc, char *argv[])
{
    int s,i,j;
    srand(10*getpid());

    s=(float)319*rand()/32767/32767/2+1;
    for(i=0; i<total_instruction; i+=4)
    {
        if(s<0||s>319)
        {
            printf("When i==%d,Error,s==%d\n",i,s);
            exit(0);
        }
        a[i]=s;
        a[i+1]=a[i]+1;
        a[i+2]=(float)a[i]*rand()/32767/32767/2;
        a[i+3]=a[i+2]+1;
        s=(float)(318-a[i+2])*rand()/32767/32767/2+a[i+2]+2;
        if((a[i+2]>318)||(s>319))
            printf("a[%d+2],a number which is:%d and s==%d\n",i,a[i+2],s);
    }
    for(i=0; i<total_instruction; i++)
    {
        page[i]=a[i]/10;
        offset[i]=a[i]%10;
    }
    for(i=4; i<=32; i++)
    {
        printf("%2d page frames  ",i);
        FIFO(i);
        LRU(i);
        LFU(i);
        NUR(i);
        printf("\n");
    }
    return 0;
}

void initialize(int total_pf)
{
    int i;
    diseffect=0;

    for(i=0; i<total_vp; i++)
    {
        pl[i].pn=i;
        pl[i].pfn=INVALID;
        pl[i].count=0;
        pl[i].time=-1;
    }
    for(i=0; i<total_pf-1; i++)
    {
        pfc[i].next=&pfc[i+1];
        pfc[i].pfn=i;
    }
    pfc[total_pf-1].next=NULL;
    pfc[total_pf-1].pfn=total_pf-1;
    freepf_head=&pfc[0];
}

void FIFO(int total_pf)
{
    int i,j;
    pfc_type *p;
    initialize(total_pf);
    busypf_head=busypf_tail=NULL;
    for(i=0; i<total_instruction; i++)
    {
        if(pl[page[i]].pfn==INVALID)// instruction i is in page page[i]
            //page don't have page frame
        {
            diseffect+=1;//miss +1
            if(freepf_head==NULL)
                //no free page frame
            {
                p=busypf_head->next;
                pl[busypf_head->pn].pfn=INVALID;
                freepf_head=busypf_head;
                freepf_head->next=NULL;
                busypf_head=p;
            }
            p=freepf_head->next;
            freepf_head->next=NULL;
            freepf_head->pn=page[i];//fit
            pl[page[i]].pfn=freepf_head->pfn;
            if(busypf_tail==NULL)//put used page frame to busy
                busypf_head=busypf_tail=freepf_head;
            else
            {
                busypf_tail->next=freepf_head;
                busypf_tail=freepf_head;
            }
            freepf_head=p;
        }
    }
    printf("FIFO: %6.4f ", 1-(float)diseffect/320);
}

void LRU(int total_pf)
{
    int min,minj,i,j,present_time;
    initialize(total_pf);
    present_time=0;

    for(i=0; i<total_instruction; i++)
    {
        if(pl[page[i]].pfn==INVALID)// instruction i is in page page[i]
        {
            diseffect++; //miss +1
            if(freepf_head==NULL)
            {
                min=32767;
                for(j=0; j<total_vp; j++)
                {
                    if(min>pl[j].time&&pl[j].pfn!=INVALID)
                    {
                        min=pl[j].time;
                        minj=j;
                    }
                }
                freepf_head=&pfc[pl[minj].pfn];
                pl[minj].pfn=INVALID;
                pl[min].time=-1;
                freepf_head->next=NULL;
            }
            pl[page[i]].pfn=freepf_head->pfn;
            pl[page[i]].time=present_time;
            freepf_head=freepf_head->next;
        }
        else
            pl[page[i]].time=present_time;
        present_time++;
    }
    printf("LRU:%6.4f ",1-(float)diseffect/320);
}

void LFU(int total_pf)
{
    int i,j,min,minpage;
    pfc_type *t;

    initialize(total_pf);
    for(i=0; i<total_instruction; i++)
    {
        if(pl[page[i]].pfn==INVALID)
        {
            diseffect++;
            if(freepf_head==NULL)
            {
                min=32767;
                for(j=0; j<total_vp; j++)
                {
                    if(min>pl[j].count&&pl[j].pfn!=INVALID)
                    {
                        min=pl[j].count;
                        minpage=j;
                    }
                    pl[j].count=0;
                }
                freepf_head=&pfc[pl[minpage].pfn];
                pl[minpage].pfn=INVALID;
                freepf_head->next=NULL;
            }
            pl[page[i]].pfn=freepf_head->pfn;
            freepf_head=freepf_head->next;
            pl[page[i]].count++;
        }
        else
            pl[page[i]].count++;
    }
    printf("LFU:%6.4f", 1-(float)diseffect/320);
}

void NUR(int total_pf)
{
    int i,j,visited[32];
    pfc_type *p = NULL;
    initialize(total_pf);
    busypf_head=busypf_tail=NULL;
    for(j=0; j<32; j++) //clear
        visited[j] = 0; //visited[1] = 1 means pageframe 1 is visited 1

    for(i=0; i<total_instruction; i++)
    {
        if( i % 10 ==0)
            for(j=0; j<32; j++) //clear
                visited[j] = 0;
        if(pl[page[i]].pfn==INVALID)// not in pageframe
        {
            diseffect++;//miss +1
            if(freepf_head==NULL)//no free pageframe
            {

                for(p = busypf_head; p != busypf_tail; p = p->next)
                {
                    if(visited[p->pn] == 1)
                        continue;
                    else
                    {
                        freepf_head=&pfc[pl[i].pfn];
                        pl[i].pfn=INVALID;
                        freepf_head->next=NULL;
                    }
                }
            }

            //have free pageframe
            pl[page[i]].pfn=freepf_head->pfn;
            freepf_head=freepf_head->next;
            pl[page[i]].count++;
            visited[pl[page[i]].pn]++;
        }
        else
            pl[page[i]].count++;
    }
    printf(" NUR:%6.4f", 1-(float)diseffect/320);
}

