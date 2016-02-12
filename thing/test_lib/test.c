#include "test.h"


char *buffer;
char copy[1000];
int glob_len;

unsigned char *buf2;
unsigned char copy2[1000];


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


int assign2(const unsigned char* arg, int len)
{
   int j;
   glob_len = len;
   buf2 = (char *)arg;

   for (j=0; j < len; j++)
   {
      copy2[j] = arg[j];
   }
   return check2();
}


int check2()
{
   int j;
   int result;

   result = 1;
   for (j=0; j < glob_len; j++)
      if (copy2[j] != buf2[j])
         result = 0;
   return result;
}
