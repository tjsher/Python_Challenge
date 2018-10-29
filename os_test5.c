#include<stdio.h>
#include<sys/types.h>
#include<sys/msg.h>
#include<sys/ipc.h>
#include <sys/shm.h>
#include<stdlib.h>
#include<wait.h>
#include <unistd.h>
#define SHMKEY 75

int shmid,i;
int *addr;

void CLIENT()
{
  int j ;
  shmid = shmget(SHMKEY,1024,0777|IPC_CREAT);
  addr = shmat(shmid,0,0);
  char array[11] = {'H','E','L','L','O','!','W','O','R','L','D'};
  for(j=10;j>=0;j--)
  {
    while(*addr != -1);
    printf("(CLIENT)sent : %c\n", array[10-j]);
    *addr = array[10-j];
  }
  exit(0);
}

void SERVER()
{
  shmid = shmget(SHMKEY,1024,0777|IPC_CREAT);
  addr = shmat(shmid,0,0);
  do{
    *addr = -1;
    while(*addr == -1);
    printf("(SERVER) received : %c\n",*addr);
  }while(*addr);
  shmctl(shmid,IPC_RMID,0);
  exit(0);
}

int main()
{
  while((i = fork()) == -1);
  if(!i)SERVER();
  else
  {
        while((i = fork()) == -1);
        if(!i) CLIENT();
        else
        {
          wait(0);
          wait(0);
        }
  }
}
