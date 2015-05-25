#include <stdio.h>

int x;

void test() {
  x = 21;
  printf("%d", x);
  int x;
  printf("%d", x);
  x = 42;
  printf("%d", x);
}

int main() {
  test();
  printf("%d", x);
  return 0;
}
