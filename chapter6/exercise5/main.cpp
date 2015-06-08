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

// Compilation Error
// enum EnumBits {
//   TWO = 2,
//   FOUR = 4,
//   EIGHT = 8,
// };

int main(void) {
  cout << (ONE + TWO) << endl;    // 3
  cout << (FOUR - TWO) << endl;   // 2
  cout << (TWO * EIGHT) << endl;  // 16
  cout << (EIGHT / TWO) << endl;  // 4
  cout << (ONE | TWO) << endl;    // 3
  cout << (TWO & FOUR) << endl;   // 0
  cout << (TWO ^ EIGHT) << endl;  // 10
  cout << (EIGHT << 1) << endl;   // 16
  cout << (EIGHT >> 1) << endl;   // 4

  EnumNumbers num = ONE;
  cout << num << endl;            // 1
  num = TWO;
  cout << num << endl;            // 2

  // compilation error
  // num = 10;
  // cout << num << endl;

  num = (EnumNumbers) 1;
  cout << num << endl;            // 1

  num = (EnumNumbers) 10;
  cout << num << endl;            // 10 (not defined)

  num = (EnumNumbers) 9;
  cout << num << endl;            // 9

  num = (EnumNumbers) -10;
  cout << num << endl;            // -10 (not defined)
  return 0;
}
