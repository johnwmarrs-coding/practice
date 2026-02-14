import java.util.ArrayList;
import java.util.Random;

public class SegmentTree {
    Node root = null;
    ArrayList<Integer> data = new ArrayList<Integer>(0);

    public SegmentTree(ArrayList<Integer> data) {
        this.data = data;
        root = new Node(0, data.size(), data);
    }

    public void print() {
        root.print();
    }


    public static void main(String[] args) {
        int numElements =  10000;
        int valMin = 0;
        int valMax = 10;

        ArrayList<Integer> myList = new ArrayList<Integer>();
        Random random = new Random();

        for (int i = 0; i < numElements; i++) {
            myList.add(random.nextInt(valMin, valMax));
        }

        System.out.println("Creating SegmentTree for: ");
        System.out.println(myList.toString());

        SegmentTree tree = new SegmentTree(myList);
//        tree.print();

    }
}

class Node {
    Integer value;
    Integer startIndex;
    Integer endIndex;
    ArrayList<Integer> data;

    Node left = null;
    Node right = null;

    public Node(Integer start, Integer end, ArrayList<Integer> data) {
        startIndex = start;
        endIndex = end;
        this.data = data;
        value = sumRange();

        int middleIndex = (startIndex + endIndex) / 2;
        if (this.data.size() > 1) {
//            System.out.println(this.data);
//            System.out.println("Start: " + startIndex + " Mid:" + middleIndex + " End: " + endIndex);

            this.left = new Node(startIndex, middleIndex, new ArrayList<Integer>(this.data.subList(0, this.data.size() / 2)));
            this.right = new Node(middleIndex, endIndex, new ArrayList<Integer>(this.data.subList(this.data.size() / 2, this.data.size())));

        }
    }

    public void print() {
        System.out.println("Node [" + startIndex + ":" + (endIndex - 1) + "](" + value + ")");
        if (left != null) {
            left.print();
        }
        if (right != null) {
            right.print();
        }
    }

    private Integer sumRange(){
        Integer total = 0;
        for (int i = 0; i < data.size(); i++) {
            total += this.data.get(i);
        }
        return total;
    }
}
