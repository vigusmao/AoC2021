import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Day1_1 {

    public static int solve(String inputFilePath) throws FileNotFoundException {
        File inputFile = new File(inputFilePath);
        Scanner sc = new Scanner(inputFile);

        int result = 0;
        Integer lastMeasure = null;

        while (sc.hasNext()) {
            String line = sc.next();
            int measure = Integer.parseInt(line);
            if (lastMeasure != null && measure > lastMeasure) {
                result++;
            }
        lastMeasure = measure;
        }

        return result;
    }

    public static void main(String[] args) throws FileNotFoundException {
        System.out.println(solve("/Users/viniciusgusmao/Documents/AoC2021/1.txt"));
    }
}
