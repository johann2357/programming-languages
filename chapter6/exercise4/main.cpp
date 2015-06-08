#include <stdio.h>
#include <vector>
#include "timer.h"

/**
 *
 *
 * $ ./rangechecking.out 
 * The code to be timed took 7.854775e+00 seconds
 * $ ./norangechecking.out 
 * The code to be timed took 2.431091e+00 seconds
 *
 * Con esto se puede ver que si se hace subscript range checking, el tiempo
 * de ejecucion es mucho mayor
 *
**/

#define N 20000

int main() {
  double start, finish, elapsed;
  std::vector< std::vector<int> > test(
    N,
    std::vector<int>(N)
  );
  GET_TIME(start);
  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < N; ++j) {
      test[i][j] += i * j;
    }
  }
  GET_TIME(finish);
  elapsed = finish - start;
  printf("The code to be timed took %e seconds\n", elapsed);
  return 0;
}
