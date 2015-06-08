#include <stdio.h>
#include "timer.h"

#define N 10000

int my_array[N][N] = {0};

/**
 * El acceso con aritmetica de punteros es mucho mas rapido
 * Sin embargo el primero es mucho mas legible y mas confiable que el segundo,
 * ya que esos calculos los hace el compilador y no se hacen manualmente
 *
 * OUTPUT:
 * simple_access took 0.209024 seconds
 * pointer_access took 0.197927 seconds
 *
**/

void simple_access() {
  for(int i = 0; i < N ; ++i){
    for(int j = 0; j < N ; ++j){
      my_array[i][j];
    }
  }
  return;
}

void pointer_access() {
  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < N; ++j) {
      *(my_array + i + j);
    }
  }
  return;
}

int main() {
  double start, finish, elapsed;
  GET_TIME(start);
  simple_access();
  GET_TIME(finish);
  elapsed = finish - start;
  printf("simple_access took %2f seconds\n", elapsed);

  start = 0;
  finish = 0;
  GET_TIME(start);
  pointer_access();
  GET_TIME(finish);
  elapsed = finish - start;
  printf("pointer_access took %2f seconds\n", elapsed);

  return 0;
}
