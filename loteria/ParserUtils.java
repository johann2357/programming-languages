import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


public class ParserUtils {
	
	private List<String> parse_file(String filename) {
		List<String> parsed_data = new ArrayList<String>();
		// Construct BufferedReader from FileReader
		BufferedReader br = null;
		try {
			br = new BufferedReader(new FileReader(filename));
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	 
		String line = null;
		try {
			while ((line = br.readLine()) != null) {
				parsed_data.add(line);
			}
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	 
		try {
			br.close();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return parsed_data;
	}

	public List<List<String>> parse_bets(String filename) {
		List<String> bets = parse_file(filename);
		List<List<String>> result = new ArrayList<>();
		for (String bet : bets) {
				result.add(Arrays.asList(bet.split("\\s+")));
		}
		return result;
	}
	public List<String> parse_result(String filename) {
		List<String> res = parse_file(filename);
		return Arrays.asList(res.get(0).split("\\s+"));
	}
}
