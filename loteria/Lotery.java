import java.util.ArrayList;
import java.util.Scanner;

public class Lotery {
	public static void main(String [] args) {
		String s;

		Scanner in = new Scanner(System.in);

		System.out.println("Enter the lottery");
		s = in.nextLine();

		ChooserUtils utils = new ChooserUtils();
		ArrayList<String> lottery = utils.get_lotery_options();
		ParserUtils parser = new ParserUtils();
		parser.parse_file(lottery.get(0));
		parser.parse_file(lottery.get(1));
	}
}
