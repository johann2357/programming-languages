import java.util.ArrayList;

public class Quina implements LoteryInterface {

    ArrayList<String[]> bets;
    String[] result;
    float[] prices = {0.75f, 3.0f, 7.5f};
    float[] partitions = {0.25f, 0.25f, 0.35f};
    float[] partitions_amount;
    float total_per = 104.5f;
    float total_amount = 104.5f;

    private void get_amounts() {
    }

    private void get_results() {
    }

    public void parse_bets(ArrayList<String> bs) {
        for (String s : bs) {
            // FIXME: throws a NullPointerException ... WAT
            bets.add(s.split(" "));
        }
        get_amounts();
        return;
    }


    public void parse_result(ArrayList<String> r) {
        result = r.get(0).split(" ");
        get_results();
        return;
    }
}
