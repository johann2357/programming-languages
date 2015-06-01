#include <stdio.h>

int main (int argc, char * argv[]) {
  /**
   * El compilador no comprueba si es que son diferentes tipos de ints por lo
   * que esta en manos del programador usar eso cuidadosamente
   *
   * Output
   * long2 = 1 
   * int_ = 1286608618
  **/
  int int_ = 1;
  long int long1 = 9876543210, long2;
  long2 = int_;
  int_ = long1;
  printf("long2 = %ld \n", long2);
  printf("int_ = %d \n", int_); 
  return 0;
}
