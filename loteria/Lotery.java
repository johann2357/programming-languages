import java.util.ArrayList;
import java.util.Scanner;

public class Lotery {
	public static void main(String [] args) {
		String s;

		Scanner in = new Scanner(System.in);

		System.out.println("Enter the lottery");
		s = in.nextLine();

		ChooserUtils utils = new ChooserUtils();
		ArrayList<String> lottery = utils.get_lotery_options(s);
		ParserUtils parser = new ParserUtils();
		ArrayList<String> bets = parser.parse_file(lottery.get(0));
		for (String bet : bets) {
			System.out.println(bet);
		}
		ArrayList<String> result = parser.parse_file(lottery.get(1));
		for (String r : result) {
			System.out.println(r);
		}
	}
}
