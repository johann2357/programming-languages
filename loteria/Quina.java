import java.util.ArrayList;
import java.util.List;

public class Quina implements LoteryInterface {

    List<List<String>> bets = null;
    List<String> result = null;
    float[] prices = {0.75f, 3.0f, 7.5f};
    float[] partitions = {0.25f, 0.25f, 0.35f};
    float[] partitions_amount;
    float total_per = 104.5f;
    float total_amount = 104.5f;

    private void get_amounts() {
    }

    private void get_results() {
    }

    public void set_bets(List<List<String>> bs) {
        bets = bs;
        return;
    }


    public void set_result(List<String> r) {
        result = r;
        return;
    }
}
