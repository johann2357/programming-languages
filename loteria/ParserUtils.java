import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;


public class ParserUtils {
	
	public ArrayList<String> parse_file(String filename) {
		ArrayList<String> parsed_data = new ArrayList<String>();
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
}
