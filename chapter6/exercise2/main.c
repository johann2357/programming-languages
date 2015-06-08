#include <stdio.h>
#include <stdlib.h>  

int main () {
  char * p;
  p = (char *) malloc (sizeof (char));
  if (p == NULL)
  {
    printf ("Failed to allocate space for %d bytes", sizeof (char));
    return 1;
  }
  *p = 'j';
  printf ("%p -> ", p);
  printf ("%c \n", *p);
  free (p);
  printf ("%p -> ", p);
  printf ("%c \n", *p);
  return 0;
}
