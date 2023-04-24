// Import required libraries
import java.util.Scanner;

// Declare the Node class
class Node {
    String data;
    int next;
}

class OrderedLinkedList {
    // constant null pointer
    static final int NULL_POINTER = -1;

    // Declare global pointers
    static int head = NULL_POINTER;
    static int tail = NULL_POINTER;
    static int free = NULL_POINTER;

    // Create a list of 10 nodes, lst[0] to lst[9]
    static Node[] lst = new Node[10];

    public static void main(String[] args) {
        initFreeList();
        int option = 0;
        Scanner scanner = new Scanner(System.in);

        while (option != 6) {
            System.out.println("1. Add a node");
            System.out.println("2. Delete a node");
            System.out.println("3. Print the list");
            System.out.println("4. Print the array");
            System.out.println("5. Search an item");
            System.out.println("6. Exit");

            System.out.print("Enter your option: ");
            option = scanner.nextInt();

            if (option == 1) {
                System.out.print("Enter the item to be added: ");
                String item = scanner.next();
                addListItem(item);
            } else if (option == 2) {
                System.out.print("Enter the item to be deleted: ");
                String item = scanner.next();
                deleteListItem(item);
            } else if (option == 3) {
                printList();
            } else if (option == 4) {
                printArray();
            } else if (option == 5) {
                System.out.print("Enter the item to search for: ");
                String item = scanner.next();
                int index = searchListItem(item);
                if (index == NULL_POINTER) {
                    System.out.println("Item not found.");
                } else {
                    System.out.println("Item found at index " + index);
                }
            } else if (option == 6) {
                System.out.println("Goodbye!");
            } else {
                System.out.println("Invalid option");
            }
            System.out.println();
        }

        scanner.close();
    }

    // Initialize the free list
    static void initFreeList() {
        free = 0;
        head = NULL_POINTER;
        tail = NULL_POINTER;

        for (int i = 0; i < 10; i++) {
            lst[i] = new Node();
        }

        for (int i = 0; i < 9; i++) {  // 0 to 8
            lst[i].next = i + 1;
        }
        lst[9].next = NULL_POINTER;
    }

    // Add a node in ascending order to the list
    static void addListItem(String item) {
        // Check if there is an available node
        if (free == NULL_POINTER) {
            System.out.println("List is full. Cannot add more items.");
            return;
        }

        // Check if the list is empty
        if (head == NULL_POINTER) {
            head = free;
            tail = free;
            free = lst[free].next;
            lst[head].data = item;
            lst[head].next = NULL_POINTER;
            return;
        }

        // Check if the item is to be added at the head
        if (item.compareTo(lst[head].data) < 0) {
            int temp = lst[free].next;
            lst[free].data = item;
            lst[free].next = head;
            head = free;
            free = temp;
            return;
        }

        // Check if the item is to be added
    // at the tail
    if (item.compareTo(lst[tail].data) > 0) {
        int temp = lst[free].next;
        lst[free].data = item;
        lst[free].next = NULL_POINTER;
        lst[tail].next = free;
        tail = free;
        free = temp;
        return;
    }

    // Check if the item is to be added in the middle
    // Find the node before the insertion point
    int current = head;
    while (item.compareTo(lst[lst[current].next].data) > 0) {
        current = lst[current].next;
    }

    // Insert the node
    int temp = lst[free].next;
    lst[free].data = item;
    lst[free].next = lst[current].next;
    lst[current].next = free;
    free = temp;
}

// Print the list
static void printList() {
    int current = head;
    while (current != NULL_POINTER) {
        System.out.print(lst[current].data + ", ");
        current = lst[current].next;
    }
    System.out.println();
}

// Search for a list item
static int searchListItem(String item) {
    int current = head;
    while (current != NULL_POINTER) {
        if (lst[current].data.equals(item)) {
            return current;
        }
        current = lst[current].next;
    }
    return NULL_POINTER;
}

// Print the lst[] array and related pointers
static void printArray() {
    System.out.println("lst[] array:");
    System.out.println("index\tdata\tnext");
    for (int i = 0; i < 10; i++) {
        System.out.println(i + "\t" + lst[i].data + "\t" + lst[i].next);
    }
    System.out.println();
    System.out.println("head = " + head);
    System.out.println("tail = " + tail);
    System.out.println("free = " + free);
}

// Delete a node from the list
static void deleteListItem(String item) {
    // Check if the list is empty
    if (head == NULL_POINTER) {
        System.out.println("List is empty");
        return;
    }

    // Check if the item is to be deleted from the head
    if (item.equals(lst[head].data)) {
        int temp = head;
        head = lst[head].next;
        lst[temp].next = free;
        free = temp;
        lst[free].data = "";
        return;
    }

    // Check if the item is to be deleted from the tail
    if (item.equals(lst[tail].data)) {
        int current = head;
        while (lst[current].next != tail) {
            current = lst[current].next;
        }
        lst[current].next = NULL_POINTER;
        lst[tail].next = free;
        free = tail;
        tail = current;
        lst[free].data = "";
        return;
    }

    // Check if the item is to be deleted from the middle
    int current = head;
    while (!item.equals(lst[lst[current].next].data)) {
        current = lst[current].next;
        if (lst[current].next == NULL_POINTER) {
            System.out.println("Item not found");
            return;
        }
    }

    // Delete the node
    int temp = lst[current].next;
    lst[current].next = lst[lst[current].next].next;
    lst[temp].next = free;
    free = temp;
    lst[free].data = "";
}
}