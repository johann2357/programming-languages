import java.lang.System;
public class Ch5Pe5 {
   public static int x = 0;
   private static void test() {
      System.out.println(x);
      x = 21;
      System.out.println(x);
      int x;
      x = 42;
      System.out.println(x);
   }
   public static void main(String [] args) {
      test();
      System.out.println(x);
   }
}
