#include <iostream>
using namespace std;

enum EnumNumbers {
  ZERO,
  ONE,
  TWO,
  THREE,
  FOUR,
  FIVE,
  SIX,
  SEVEN,
  EIGHT,
  NINE,
};

enum EnumStates {
  OK = 200,
  NOTFOUNT = 404,
  UNAVAILABLE = 503,
};

enum EnumErrors {
  NONE = 0,
  FAILED = 300,
  NORESPONSE = 500,
};


int main(void) {
  EnumNumbers num = ONE;
  EnumErrors err = FAILED;
  EnumStates ss = OK;
  num = TWO;
  if (num == TWO) {
    err = NONE;
  }
  if (ss == UNAVAILABLE) {
    err = NORESPONSE;
  }
  return 0;
}
