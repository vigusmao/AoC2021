import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.Stack;

public class Day10_2 {

    static Map<Character, Character> OPENING_BY_CLOSING = new HashMap<>();
    static Map<Character, Integer> SCORE_BY_CLOSING = new HashMap<>();
    static Map<Character, Integer> SCORE_BY_OPENING = new HashMap<>();

    static {
        OPENING_BY_CLOSING.put('>', '<');
        OPENING_BY_CLOSING.put(')', '(');
        OPENING_BY_CLOSING.put('}', '{');
        OPENING_BY_CLOSING.put(']', '[');

        SCORE_BY_CLOSING.put(')', 3);
        SCORE_BY_CLOSING.put(']', 57);
        SCORE_BY_CLOSING.put('}', 1197);
        SCORE_BY_CLOSING.put('>', 25137);

        SCORE_BY_OPENING.put('(', 1);
        SCORE_BY_OPENING.put('[', 2);
        SCORE_BY_OPENING.put('{', 3);
        SCORE_BY_OPENING.put('<', 4);
    }

    public static long complete(String line) {
        long result = 0;
        Stack<Character> stack = new Stack<>();
        for (char c : line.toCharArray()) {
            Character opening = OPENING_BY_CLOSING.get(c);
            if (opening != null) {
                if (stack.isEmpty() || stack.peek() != opening) {
                    return -1;
                } else {
                    stack.pop();
                }
            } else {
                stack.push(c);
            }
        }
        while (!stack.isEmpty()) {
            char c = stack.pop();
            result *= 5;
            result += SCORE_BY_OPENING.get(c);
        }
        return result;
    }

    public static long solve(String inputFilePath) throws FileNotFoundException {
        File inputFile = new File(inputFilePath);
        Scanner sc = new Scanner(inputFile);

        List<Long> scores = new ArrayList<>();

        while (sc.hasNext()) {
            String line = sc.nextLine();
            long score = complete(line);
            if (score != -1) {
                scores.add(score);
            }
        }

        return quickSelect(scores, 0, scores.size() - 1, scores.size() / 2 + 1,
                Comparator.comparingLong(Long::longValue));
    }

    private static <T> T quickSelect(List<T> list, int startIndex, int endIndex, int k, Comparator<T> comparator) {
        if (list == null || list.isEmpty() || endIndex < startIndex)
            return null;

        int targetIndex = Math.min(k - 1, endIndex - startIndex);

        while (startIndex < endIndex) {
            int reader = startIndex;
            int writer = endIndex;
            T pivot = list.get((reader + writer) / 2);

            while (reader < writer) {
                if (comparator.compare(list.get(reader), pivot) >= 0) {
                    // swaps the keys
                    T tmpKey = list.get(writer);
                    list.set(writer, list.get(reader));
                    list.set(reader, tmpKey);
                    writer--;
                } else {
                    reader++;
                }
            }

            if (comparator.compare(list.get(reader), pivot) > 0) {
                reader--;
            }

            if (reader >= targetIndex) {
                endIndex = reader;
            } else {
                startIndex = reader + 1;
            }
        }

        return list.get(targetIndex);
    }

    public static void main(String[] args) throws FileNotFoundException {
        System.out.println(solve("/Users/viniciusgusmao/Documents/AoC2021/10.txt"));
    }
}
