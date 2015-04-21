import java.util.ArrayList;
import java.util.List;

public interface LoteryInterface {

	List<List<String>> bets = null;
	List<String> result = null;

	public void set_bets(List<List<String>> bs);
	public void set_result(List<String> r);

}
