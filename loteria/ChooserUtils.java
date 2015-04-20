import java.util.ArrayList;


public class ChooserUtils {
	
	public String get_bets_file_location(String directory) {
		return directory + "/bets.txt";
	}
	
	public String get_result_file_location(String directory) {
		return directory + "/results.txt";
	}
	
	public ArrayList<String> get_lotery_options(String directory) {
		ArrayList<String> files = new ArrayList<String>();
		files.add(get_bets_file_location(directory));
		files.add(get_result_file_location(directory));
		return files;
	}

}
