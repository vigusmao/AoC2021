import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Day2_2 {

    public static long solve(String inputFilePath) throws FileNotFoundException {
        File inputFile = new File(inputFilePath);
        Scanner sc = new Scanner(inputFile);

        long hor = 0, depth = 0, aim = 0;

        while (sc.hasNext()) {
            String line = sc.nextLine();
            String[] tokens = line.split("\\s");
            String command = tokens[0];
            long amount = Long.parseLong(tokens[1]);

            switch (command) {
                case "forward":
                    hor += amount;
                    depth += amount * aim;
                    break;
                case "down":
                    aim += amount;
                    break;
                case "up":
                    aim -= amount;
                    break;
            }
        }

        return hor * depth;
    }

    public static void main(String[] args) throws FileNotFoundException {
        System.out.println(solve("/Users/viniciusgusmao/Documents/AoC2021/2.txt"));
    }
}
