import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Day2_1 {

    public static int solve(String inputFilePath) throws FileNotFoundException {
        File inputFile = new File(inputFilePath);
        Scanner sc = new Scanner(inputFile);

        int hor = 0, depth = 0;

        while (sc.hasNext()) {
            String line = sc.nextLine();
            String[] tokens = line.split("\\s");
            String command = tokens[0];
            int amount = Integer.parseInt(tokens[1]);

            switch (command) {
                case "forward":
                    hor += amount;
                    break;
                case "down":
                    depth += amount;
                    break;
                case "up":
                    depth -= amount;
                    break;
            }
        }

        return hor * depth;
    }

    public static void main(String[] args) throws FileNotFoundException {
        System.out.println(solve("/Users/viniciusgusmao/Documents/AoC2021/2.txt"));
    }
}
