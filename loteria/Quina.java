import java.util.Arrays;
import java.util.List;

public class Quina implements LoteryInterface {

    List<List<String>> bets = null;
    List<String> result = null;
    List<Float> prices = Arrays.asList(0.75f, 3.0f, 7.5f);
    List<Float> partitions = Arrays.asList(0.25f, 0.25f, 0.35f);
    List<String> partitions_name = Arrays.asList("Terno", "Quadra", "Quina");
    List<Integer> partitions_count = Arrays.asList(0, 0, 0);
    Float total_per = 104.5f;
    Float total_prices_per = 32.2f;
    Float total_amount = 0f;
    Float total_prices_amount = 0f;

    private void get_amounts() {
        for (List<String> p : bets) {
            total_amount += prices.get(p.size() - 5);
        }
        total_prices_amount = total_amount * total_per / 100;
        total_prices_amount = total_prices_amount * total_prices_per / 100;
    }

    private void get_results() {
        for (List<String> bet : bets) {
            int count = 0;
            for (String n : bet) {
                if (result.contains(n)) {
                    count++;
                }
            }
            if (count > 2) {
                partitions_count.set(count - 3, (partitions_count.get(count - 3) + 1));
            }
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
