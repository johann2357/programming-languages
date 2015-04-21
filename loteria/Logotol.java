import java.util.Arrays;
import java.util.List;

public class Logotol implements LoteryInterface{

    List<List<String>> bets = null;
    List<String> result = null;
    List<Float> prices = Arrays.asList(0.5f, 1.0f, 2.0f);
    List<Float> partitions = Arrays.asList(0.3f, 0.3f, 0.4f);
    List<String> partitions_name = Arrays.asList("1º (5 acertos)", "2º (4 acertos)", "1º (5 acertos)");
    List<Integer> partitions_count = Arrays.asList(0, 0, 0);
    Float total_per = 104.4f;
    Float total_prices_per = 28.0f;
    Float total_amount = 0f;
    Float total_prices_amount = 0f;

    private void get_amounts() {
        for (List<String> p : bets) {
            total_amount += prices.get(Integer.parseInt(p.get(0)) / 2);
        }
        total_prices_amount = total_amount * total_per / 100;
        total_prices_amount = total_prices_amount * total_prices_per / 100;
    }

    private void get_results() {
        for (int i = 1; i < bets.size() ; i++) {
            int count = 0;
            for (int j = 1; i < bets.get(i).size() ;) {
                if (result.get(j) == bets.get(i).get(j - 1)) {
                    count++;
                }
                j += 3;
            }
            partitions_count.set(count - 3, (partitions_count.get(count - 3) + 1));
        }
    }

    public void print_game() {
        get_amounts();
        get_results();
        System.out.println(total_amount);
        System.out.println(total_prices_amount);
        for (int i = 2; i >= 0; i--) {
            System.out.println(
                partitions_name.get(i) + " " + partitions_count.get(i) + " " +
                (partitions.get(i) * total_prices_amount) / partitions_count.get(i)
            );
        }
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
