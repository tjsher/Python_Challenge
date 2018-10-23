#include<stdio.h>
#include<sys/types.h>
#include<sys/msg.h>
#include<sys/ipc.h>
#include<stdlib.h>
#include<wait.h>
#include <unistd.h>
#define MSGKEY 75

struct msgform
{   long mtype;
    char *mtrex;
}msg;

int msgqid,i;

void CLIENT()
{    int i;
     msgqid=msgget(MSGKEY, 0777|IPC_CREAT);
     for(i=10;i>=1;i--)
	{  msg.mtype=i;
     msg.mtrex = "Message from client ";
	   printf("(client)sent\n");
           msgsnd(msgqid,&msg, 1024,0);
	}
	exit(0);
}

void SERVER()
{   msgqid=msgget(MSGKEY,0777|IPC_CREAT);
    do
	{  msgrcv(msgqid,&msg,1024,0,0);
	   printf("(server)received, %s\n",msg.mtrex);
	}while (msg.mtype!=1);
	msgctl(msgqid,IPC_RMID,0);
	exit(0);
}
void main()
{   while((i=fork())==-1);
    if(!i)SERVER();
    else
	{while((i=fork())==-1);
  	 if(!i)CLIENT();
	 else
		{wait(0);
		 wait(0);
		}
	}
}
