import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Day1_2 {

    public static int solve(String inputFilePath) throws FileNotFoundException {
        File inputFile = new File(inputFilePath);
        Scanner scanner = new Scanner(inputFile);

        int result = 0;
        Integer[] lastMeasures = new Integer[3];
        while (scanner.hasNext()) {
            int measure = scanner.nextInt();
            if (lastMeasures[0] != null && measure > lastMeasures[0]) {
                ++result;
            }
            lastMeasures[0] = lastMeasures[1];
            lastMeasures[1] = lastMeasures[2];
            lastMeasures[2] = measure;
        }
        return result;
    }

    public static void main(String[] args) throws FileNotFoundException {
        System.out.println(solve("/Users/viniciusgusmao/Documents/AoC2021/1.txt"));
    }
}
