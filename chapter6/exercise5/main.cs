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
    
    enum EnumBits {
        TWO = 2,
        FOUR = 4,
        EIGHT = 8,
    };



    static void Main()
    {
        // compilation error
        // Console.WriteLine((EnumNumbers.ONE + EnumNumbers.TWO));
        
        Console.WriteLine((EnumNumbers.FOUR - EnumNumbers.TWO));   // 2
        
        // compilation error
        // Console.WriteLine((EnumNumbers.TWO * EnumNumbers.EIGHT));
        // Console.WriteLine((EnumNumbers.EIGHT / EnumNumbers.TWO));
        
        Console.WriteLine((EnumNumbers.ONE | EnumNumbers.TWO));    // THREE
        Console.WriteLine((EnumNumbers.TWO & EnumNumbers.FOUR));   // ZERO
        Console.WriteLine((EnumNumbers.TWO ^ EnumNumbers.EIGHT));  // 10
        
        // compilation error
        // Console.WriteLine((EnumNumbers.EIGHT << 1));
        // Console.WriteLine((EnumNumbers.EIGHT >> 1));

        EnumNumbers num = EnumNumbers.ONE;
        Console.WriteLine(num);            // ONE
        num = EnumNumbers.TWO;
        Console.WriteLine(num);            // TWO
        
        // compilation error
        // num = 10;
        
        num = (EnumNumbers) 1;
        Console.WriteLine(num);            // ONE
        
        num = (EnumNumbers) 10;
        Console.WriteLine(num);            // 10
        
        num = (EnumNumbers) 9;
        Console.WriteLine(num);            // NINE
        
        // compilation error
        // num = (EnumNumbers) -10;
        // Console.WriteLine(num);

    }
}