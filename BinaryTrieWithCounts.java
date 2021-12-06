public class BinaryTrieWithCounts {

    Node root = new Node(null, null);

    public void add(String digits) {
        root.add(digits, -1);
    }

    public Node getRoot() {
        return root;
    }

    public class Node {

        Boolean value;
        boolean isFinal;

        Node trueChild;
        Node falseChild;
        Node parent;

        int countFinalDescendants;

        Node(Node parent, Boolean value) {
            this.parent = parent;
            this.value = value;
        }

        void add(String digits, int pos) {
            ++countFinalDescendants;

            if (pos == digits.length() - 1) {
                isFinal = true;
            } else {
                if (digits.charAt(pos + 1) == '1') {
                    if (trueChild == null) {
                        trueChild = new Node(this, true);
                    }
                    trueChild.add(digits, pos + 1);
                } else {
                    if (falseChild == null) {
                        falseChild = new Node(this, false);
                    }
                    falseChild.add(digits, pos + 1);
                }
            }
        }

        Node getMostCommonValueChild() {
            if (trueChild == null) {
                return falseChild;
            }
            if (falseChild == null) {
                return trueChild;
            }
            return trueChild.countFinalDescendants >= falseChild.countFinalDescendants ? trueChild : falseChild;
        }

        Node getLeastCommonValueChild() {
            if (trueChild == null) {
                return falseChild;
            }
            if (falseChild == null) {
                return trueChild;
            }
            return falseChild.countFinalDescendants <= trueChild.countFinalDescendants ? falseChild : trueChild;
        }

        long getDecimalValueFromRoot() {
            if (value == null) {
                return 0;
            }
            return (value ? 1 : 0) + (parent.getDecimalValueFromRoot() << 1);
        }
    }
}
