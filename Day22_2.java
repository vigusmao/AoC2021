import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.TreeSet;

public class Day22_2 {

    static final int X = 0;
    static final int Y = 1;
    static final int Z = 2;
    static final int START = 0;
    static final int END = 1;

    static List<Cuboid> cuboidsList = new ArrayList<>();
    static TreeSet<Event> eventsTreeSetByX = new TreeSet<>(new Comparator<Event>() {
        @Override
        public int compare(Event o1, Event o2) {
            if (o1.getX() != o2.getX()) {
                return o1.getX() - o2.getX();
            }
            return o1.priority - o2.priority;
        }
    });
    static TreeSet<Event> eventsTreeSetByY = new TreeSet<>(Comparator.comparingInt(Event::getY));
    static TreeSet<Event> eventsTreeSetByZ = new TreeSet<>(Comparator.comparingInt(Event::getZ));
    static PriorityQueue<Event> eventsPriorityQueue = new PriorityQueue<>(Comparator.comparingInt(o -> o.priority));

    public static void readCuboids(List<String> lines) {
        for (String line : lines) {
            if (line.length() == 0) {
                continue;
            }
            String[] tokens = line.split(" ");
            boolean isOn = tokens[0].equals("on");
            String[] rangesToken = tokens[1].split(",");
            String[] rangeX = rangesToken[X].substring(2).split("\\.\\.");
            String[] rangeY = rangesToken[Y].substring(2).split("\\.\\.");
            String[] rangeZ = rangesToken[Z].substring(2).split("\\.\\.");

            Cuboid cuboid = new Cuboid(
                    Integer.parseInt(rangeX[START]),
                    Integer.parseInt(rangeY[START]),
                    Integer.parseInt(rangeZ[START]),
                    Integer.parseInt(rangeX[END]),
                    Integer.parseInt(rangeY[END]),
                    Integer.parseInt(rangeZ[END]),
                    isOn);
            cuboidsList.add(cuboid);
        }

        for (int i = cuboidsList.size() - 1; i >= 0; i--) {
            Cuboid cuboid = cuboidsList.get(i);
            eventsTreeSetByX.add(new Event(cuboid, true, cuboidsList.size() - i));
            eventsTreeSetByX.add(new Event(cuboid, false, cuboidsList.size() - i));
            eventsTreeSetByY.add(new Event(cuboid, true, cuboidsList.size() - i));
            eventsTreeSetByY.add(new Event(cuboid, false, cuboidsList.size() - i));
            eventsTreeSetByZ.add(new Event(cuboid, true, cuboidsList.size() - i));
            eventsTreeSetByZ.add(new Event(cuboid, false, cuboidsList.size() - i));
        }
    }

    private static int countSwitchedOn(int y, int z) {
        boolean currentState = false;
        int currentX = Integer.MIN_VALUE;
        int countOn = 0;

        eventsPriorityQueue.clear();

        for (Event event : eventsTreeSetByX) {
            if (event.cuboid.startY > y || event.cuboid.endY < y ||
                    event.cuboid.startZ > z || event.cuboid.endZ < z) {
                continue;
            }

            int newX = event.getX();

            // computes the number of consecutive "on" cubes since the one observed last
            if (currentState) {
                int deltaX = newX - currentX;
                countOn += deltaX;
            }

            // updates the priority queue
            if (event.start) {
                eventsPriorityQueue.add(event);
            }
            while (!eventsPriorityQueue.isEmpty() && eventsPriorityQueue.peek().getEndX() < newX) {
                eventsPriorityQueue.poll();
            }

            // grabs the state of the (new) root
            if (!eventsPriorityQueue.isEmpty()) {
                currentState = eventsPriorityQueue.peek().on();
            } else {
                currentState = false;
            }

            currentX = newX;
        }

        return countOn;
    }

    private static long solve(String inputFilePath) throws FileNotFoundException {
        File inputFile = new File(inputFilePath);
        Scanner sc = new Scanner(inputFile);

        List<String> lines = new ArrayList<>();

        while (sc.hasNext()) {
            String line = sc.nextLine();
            lines.add(line);
        }

        readCuboids(lines);

        long countOn = 0;
        int currentZ = Integer.MIN_VALUE;
        long lastCountAlongXY = 0;

        for (Event eventAlongZ : eventsTreeSetByZ) {
            int z = eventAlongZ.getZ();
            int deltaZ = z - currentZ;
            if (deltaZ == 0) {
                continue;
            }
            countOn += deltaZ * lastCountAlongXY;
            currentZ = z;

            lastCountAlongXY = 0;
            long lastCountAlongX = 0;
            int currentY = Integer.MIN_VALUE;
            for (Event eventAlongY : eventsTreeSetByY) {
                int y = eventAlongY.getY();
                int deltaY = y - currentY;
                if (deltaY == 0) {
                    continue;
                }
                lastCountAlongXY += deltaY * lastCountAlongX;
                currentY = y;
                lastCountAlongX = countSwitchedOn(y, z);
            }
        }

        return countOn;
    }

    static class Cuboid {
        int startX, startY, startZ, endX, endY, endZ;
        boolean on;

        public Cuboid(int startX, int startY, int startZ, int endX, int endY, int endZ, boolean on) {
            this.startX = startX;
            this.startY = startY;
            this.startZ = startZ;
            this.endX = endX;
            this.endY = endY;
            this.endZ = endZ;
            this.on = on;
        }
    }

    static class Event {
        Cuboid cuboid;
        boolean start;
        int priority;

        public Event(Cuboid cuboid, boolean start, int priority) {
            this.cuboid = cuboid;
            this.start = start;
            this.priority = priority;
        }

        public int getX() {
            return start ? cuboid.startX : cuboid.endX + 1;
        }

        public int getY() {
            return start ? cuboid.startY : cuboid.endY + 1;
        }

        public int getZ() {
            return start ? cuboid.startZ : cuboid.endZ + 1;
        }

        public int getEndX() {
            return cuboid.endX;
        }

        public boolean on() {
            return cuboid.on;
        }
    }

    public static void main(String[] args) throws FileNotFoundException {
        System.out.println(solve("/Users/viniciusgusmao/Documents/AoC2021/22.txt"));
    }
}
