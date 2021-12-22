import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Day21_1 {

    static Die die = new Die();

    public static int solve(int pos1, int pos2) {
        int score1 = 0, score2 = 0;
        while (true) {
            pos1 = updatePos(pos1);
            score1 += pos1;
            if (score1 >= 1000) {
                break;
            }

            pos2 = updatePos(pos2);
            score2 += pos2;
            if (score2 >= 1000) {
                break;
            }
        }

        return Math.min(score1, score2) * die.getRollCount();
    }

    private static int updatePos(int pos) {
        return 1 + (pos + die.next() + die.next() + die.next() - 1) % 10;
    }

    static class Die {
        int rollCount = 0;

        int next() {
            return 1 + (rollCount++) % 100;
        }

        int getRollCount() {
            return rollCount;
        }
    }

    public static void main(String[] args) throws FileNotFoundException {
        System.out.println(solve(1, 5));
    }
}
