#include <stdio.h>

int main (int argc, char * argv[]) {
  /**
   * Se pierde presicion cuando en double y float, sin embargo la operacion
   * nos da un resultado muy cercano al esperado. El compilador no
   * da ningun tipo de warning al momento de compilar por lo que el
   * desarrollador tendra que tener cuidado
   *
   * Output
   * result = 1111.109976
  **/
  int int_ = 100;
  long int long_= 1000;
  float float_ = 10.1;
  double double_ = 1.01;
  double result = int_ + long_ + float_ + double_;
  printf("result = %lf \n", result);
  return 0;
}
