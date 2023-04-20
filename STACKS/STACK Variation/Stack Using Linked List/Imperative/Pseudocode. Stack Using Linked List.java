class StackLinkedList {

    // Main program
    public static void main(String[] args) {
        initializeStack();
        int option = 0;

        while (option != 5) {
            System.out.println("\nStack Using Linked List");
            System.out.println("1. Push");
            System.out.println("2. Pop");
            System.out.println("3. Display Stack");
            System.out.println("4. Print Linked List Array");
            System.out.println("5. Exit");
            System.out.print("Enter your choice: ");
            option = Integer.parseInt(System.console().readLine());
            switch (option) {
                case 1:
                    System.out.print("Enter integer data: ");
                    int data = Integer.parseInt(System.console().readLine());
                    push(data);
                    break;
                case 2:
                    Integer poppedData = pop();
                    if (poppedData != null) {
                        System.out.println("Popped element: " + poppedData);
                    }
                    break;
                case 3:
                    displayStack();
                    break;
                case 4:
                    displayArray();
                    break;
                case 5:
                    System.out.println("Thank You");
                    break;
                default:
                    System.out.println("Invalid Choice");
            }
        }
    }

    // Linked List Node
    static class Node {
        Integer data;
        int next;

        public Node() {
            data = null;
            next = -1;
        }
    }

    // Constants
    static final int MAX = 10;
    static final int NULL_POINTER = -1;

    // Global variables
    static int topOfStack = NULL_POINTER;
    static int head = NULL_POINTER;
    static int free = 0;

    // Stack array of nodes
    static Node[] stack = new Node[MAX];

    // Function to initialize the stack
    static void initializeStack() {
        topOfStack = NULL_POINTER;
        head = NULL_POINTER;
        free = 0;
        for (int i = 0; i < MAX - 1; i++) {
            stack[i] = new Node();
            stack[i].next = i + 1;
        }
        stack[MAX - 1] = new Node();
        stack[MAX - 1].next = NULL_POINTER;
    }

    // Function to push an element into the stack
    static void push(int data) {
        if (free == NULL_POINTER) {
            System.out.println("Stack Overflow");
            return;
        } else {
            int temp = free;
            free = stack[free].next;
            stack[temp].data = data;
            stack[temp].next = topOfStack;
            topOfStack = temp;
            if (head == NULL_POINTER) {
                head = topOfStack;
            }
        }
    }

    // Function to pop an element from the stack
    static Integer pop() {
        if (topOfStack == NULL_POINTER) {
            System.out.println("Stack Underflow");
            return null;
        } else {
            int temp = topOfStack;
            topOfStack = stack[topOfStack].next;
            stack[temp].next = free;
            free = temp;
            if (topOfStack == NULL_POINTER) {
                head = NULL_POINTER;
            }
            Integer val = stack[temp].data;
            stack[temp].data = null;
            return val;
        }
    }

    // Function to display the stack
    static void displayStack() {
        if (topOfStack == NULL_POINTER) {
            System.out.println("Stack is Empty");
            return;
        } else {
            int temp = topOfStack;
            while (temp  != NULL_POINTER) {
                if (temp == topOfStack) {
                    System.out.println(stack[temp].data + " <--");
                } else {
                    System.out.println(stack[temp].data);
                }
                temp = stack[temp].next;
            }
        }
    }

    // Function to display the array
    static void displayArray() {
        System.out.println("index\tdata\tnext");
        for (int i = 0; i < MAX; i++) {
            System.out.print(i + "\t" + stack[i].data + "\t" + stack[i].next);
            if (i == free) {
                System.out.print("\tfree");
            } else if (i == topOfStack) {
                System.out.print("\ttop_of_stack | tail_of_LL");
            } else if (i == head) {
                System.out.print("\thead");
            }
            System.out.println();
        }
        System.out.println("top_of_stack: " + topOfStack);
        System.out.println("head: " + head);
        System.out.println("free: " + free);
    }

}
/* end of program code */