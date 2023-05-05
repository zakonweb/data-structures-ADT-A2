import java.util.Scanner;

class CircularQueueLinkedList {
    // Node class to store data and the next pointer
    static class Node {
        int data;
        int nextPointer;

        Node() {
            data = 0;
            nextPointer = -1;
        }
    }

    // Constants for maximum queue size and null pointer value
    static final int MAX = 10;
    static final int NULL_POINTER = -1;

    // Queue pointers
    static int queueFront = NULL_POINTER;
    static int queueRear = NULL_POINTER;
    static int freeListHead = 0;

    // Node array to store the nodes
    static Node[] nodeList = new Node[MAX];

    public static void main(String[] args) {
        initializeNodes();
    
        int choice;
        int data;
    
        try (Scanner scanner = new Scanner(System.in)) {
            while (true) {
                System.out.println("Circular Queue using Linked List with Free List");
                System.out.println("1. Enqueue");
                System.out.println("2. Dequeue");
                System.out.println("3. Display");
                System.out.println("4. Exit");
                System.out.print("Enter your choice: ");
                choice = scanner.nextInt();
    
                switch (choice) {
                    case 1:
                        System.out.print("Enter the element to be enqueued: ");
                        data = scanner.nextInt();
                        enqueue(data);
                        break;
                    case 2:
                        data = dequeue();
                        if (data != -1) {
                            System.out.println("The dequeued element is: " + data);
                        }
                        break;
                    case 3:
                        display();
                        break;
                    case 4:
                        return;
                    default:
                        System.out.println("Invalid choice");
                }
            }
        }
    }
    
    // Initialize the nodes and the free list
    static void initializeNodes() {
        for (int i = 0; i < MAX; i++) {
            nodeList[i] = new Node();
        }

        for (int i = 0; i < MAX - 1; i++) {
            nodeList[i].nextPointer = i + 1;
        }
        nodeList[MAX - 1].nextPointer = NULL_POINTER;
    }

    // Enqueue an element into the queue
    static void enqueue(int data) {
        if (freeListHead == NULL_POINTER) {
            System.out.println("Queue is full");
        } else {
            int newNodeIndex = freeListHead;
            freeListHead = nodeList[freeListHead].nextPointer;

            nodeList[newNodeIndex].data = data;
            nodeList[newNodeIndex].nextPointer = NULL_POINTER;

            if (queueRear == NULL_POINTER) {
                queueFront = newNodeIndex;
                queueRear = newNodeIndex;
            } else {
                nodeList[queueRear].nextPointer = newNodeIndex;
                queueRear = newNodeIndex;
            }
        }
    }

    // Dequeue an element from the queue
    static int dequeue() {
        if (queueFront == NULL_POINTER) {
            System.out.println("Queue is empty");
            return -1;
        } else {
            int oldFrontIndex = queueFront;
            queueFront = nodeList[queueFront].nextPointer;

            if (queueFront == NULL_POINTER) {
                queueRear = NULL_POINTER;
            }

            nodeList[oldFrontIndex].nextPointer = freeListHead;
            freeListHead = oldFrontIndex;

            return nodeList[oldFrontIndex].data;
        }
    }

    // Display the elements in the queue
    static void display() {
        if (queueFront == NULL_POINTER) {
            System.out.println("Queue is empty");
        } else {
            System.out.print("Elements in the queue: ");

            int currentIndex = queueFront;
            while (currentIndex != NULL_POINTER) {
                System.out.print(nodeList[currentIndex].data + " ");
                currentIndex = nodeList[currentIndex].nextPointer;
            }
            System.out.println();
        }
    }
}
