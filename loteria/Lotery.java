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
		ArrayList<String> result = parser.parse_file(lottery.get(1));
		Quina game = new Quina();
		game.parse_bets(bets);
		game.parse_result(result);
	}
}
