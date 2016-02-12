#include "test.h"


char *buffer;
char copy[100];
int glob_len;


int assign(const char* arg, int len)
{
   int j;
   glob_len = len;
   buffer = (char *)arg;

   for (j=0; j < len; j++)
   {
      copy[j] = arg[j];
   }
   return check();
}

char *get_buffer()
{
   return buffer;
}

int get_len()
{
   return glob_len;
}

int check()
{
   int j;
   int result;

   result = 1;
   for (j=0; j < glob_len; j++)
      if (copy[j] != buffer[j])
         result = 0;
   return result;
}
