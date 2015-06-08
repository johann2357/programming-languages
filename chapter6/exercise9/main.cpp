#include <stdio.h>

typedef struct {
   int a;
   int b;
} Point;

typedef struct {
   int a;
   int b;
} Pair;


int main () {
  // Name equivalence
  Point x;
  Pair y;
  // x = y; // error
  return 0;
}
