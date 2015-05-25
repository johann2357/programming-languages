#include <sys/time.h>
#include <iostream>

void statically() {
  for (int i = 0; i < 100000; ++i) {
    int static my_array[1000];
  }
}

void stack() {
  for (int i = 0; i < 100000; ++i) {
    int my_array[1000];
  }
}

void heap() {
  for (int i = 0; i < 100000; ++i) {
    int* my_array = new int [1000];
  }
}

void take_time( void (*f)() ) {
  struct timeval startTime;
  struct timeval endTime;

  // get the current time - NULL because we don't care about time zone
  gettimeofday(&startTime, NULL);

  // algorithm
  (*f)();

  // get the end time
  gettimeofday(&endTime, NULL);

  // calculate time in microseconds
  double tS = startTime.tv_sec*1000000 + (startTime.tv_usec);
  double tE = endTime.tv_sec*1000000 + (endTime.tv_usec);
  std::cout << "Total Time Taken: " << tE - tS << std::endl;
}

int main(int argc, char **argv) {
  take_time(statically);
  take_time(stack);
  take_time(heap);
  return 0;
}
