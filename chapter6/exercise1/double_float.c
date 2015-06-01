#include <stdio.h>

int main (int argc, char * argv[]) {
  /**
   * El compilador no comprueba si es que son flotantes de diferente precision
   * esta en manos del programador usar eso cuidadosamente
   *
   * Output
   * double2 = 0.100000 
   * float_ = 0.123457
  **/
  float float_ = 0.1;
  double double1 = 0.123456789, double2;
  double2 = float_;
  float_ = double1;
  printf("double2 = %lf \n", double2);
  printf("float_ = %f \n", float_); 
  return 0;
}
