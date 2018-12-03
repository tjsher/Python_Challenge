#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
int main()
{int *mem = NULL;

  while(1)
  {
  mem = (int*)malloc(sizeof(int) * 1024 * 1024); //sizeof(int) = 4
  memset(mem,'0',sizeof(int) * 1024 * 1024);
  sleep(1);
}
  return 0;
}
