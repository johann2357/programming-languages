import java.util.ArrayList;
import java.util.List;
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
		List<List<String>> bets = parser.parse_bets(lottery.get(0));
		List<String> result = parser.parse_result(lottery.get(1));

		// COMMON LOTTERIES PART, JUST INSTANTIATE THE LOTTERY
		Quina game = new Quina();
		game.set_bets(bets);
		game.set_result(result);
		game.print_game();
	}
}
