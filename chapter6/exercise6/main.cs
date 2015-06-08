using System.IO;
using System;


class Program
{
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

    static void Main()
    {
        EnumNumbers num = EnumNumbers.ONE;
        EnumErrors err = EnumErrors.FAILED;
        EnumStates ss = EnumStates.OK;
        num = EnumNumbers.TWO;
        if (num == EnumNumbers.TWO) {
            err = EnumErrors.NONE;
        }
        if (ss == EnumStates.UNAVAILABLE) {
            err = EnumErrors.NORESPONSE;
        }

    }
}
