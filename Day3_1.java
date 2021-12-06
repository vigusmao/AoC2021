import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Day3_1 {

    public static long solve(String inputFilePath) throws FileNotFoundException {
        File inputFile = new File(inputFilePath);
        Scanner sc = new Scanner(inputFile);

        int[] counts = null;
        int lineCount = 0;

        while (sc.hasNext()) {
            String token = sc.nextLine();
            ++lineCount;

            if (counts == null) {
                counts = new int[token.length()];
            }

            for (int i = 0; i < token.length(); i++) {
                if (token.charAt(i) == '1') {
                    ++counts[i];
                }
            }
        }

        if (counts == null) {
            return 0;
        }

        long gamma = 0, epsilon = 0;

        float minCountFor1 = lineCount / 2f;

        long powerOfTwo = 1;
        for (int i = counts.length - 1; i >= 0; i--) {
            if (counts[i] >= minCountFor1) {
                gamma += powerOfTwo;
            } else {
                epsilon += powerOfTwo;
            }
            powerOfTwo <<= 1;
        }

        return gamma * epsilon;
    }

    public static void main(String[] args) throws FileNotFoundException {
        System.out.println(solve("/Users/viniciusgusmao/Documents/AoC2021/3.txt"));
    }
}
