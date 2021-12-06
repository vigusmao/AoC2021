import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Day3_2 {

    public static long solve(String inputFilePath) throws FileNotFoundException {
        File inputFile = new File(inputFilePath);
        Scanner sc = new Scanner(inputFile);

        BinaryTrieWithCounts trie = new BinaryTrieWithCounts();

        // adds all numbers to the trie
        while (sc.hasNext()) {
            String token = sc.next();
            trie.add(token);
        }

        // for oxygen, traverse the trie following the child node with the most descendants
        BinaryTrieWithCounts.Node oxygenNode = trie.getRoot();
        while (!oxygenNode.isFinal) {
            oxygenNode = oxygenNode.getMostCommonValueChild();
        }

        // for CO2, traverse the trie following the child node with the fewest descendants
        BinaryTrieWithCounts.Node co2Node = trie.getRoot();
        while (!co2Node.isFinal) {
            co2Node = co2Node.getLeastCommonValueChild();
        }

        return oxygenNode.getDecimalValueFromRoot() * co2Node.getDecimalValueFromRoot();
    }

    public static void main(String[] args) throws FileNotFoundException {
        System.out.println(solve("/Users/viniciusgusmao/Documents/AoC2021/3.txt"));
    }
}
