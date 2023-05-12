import java.util.Scanner;

class Main {
    static final int NULL_POINTER = -1;
    static Node[] lst = new Node[10];
    static int head = NULL_POINTER;
    static int tail = NULL_POINTER;
    static int free = NULL_POINTER;

    static class Node {
        String data;
        int next;

        public Node() {
            this.data = "";
            this.next = NULL_POINTER;
        }
    }

    public static void init_free_list() {
        free = 0;
        head = NULL_POINTER;
        tail = NULL_POINTER;
        for (int i = 0; i < 9; i++) {
            lst[i] = new Node();
            lst[i].next = i + 1;
        }
        lst[9] = new Node();
        lst[9].next = NULL_POINTER;
    }

    public static void add_list_item(String item) {
        if (free == NULL_POINTER) {
            System.out.println("List is full. Cannot add more items.");
            return;
        }

        if (head == NULL_POINTER) {
            head = free;
            tail = free;
            free = lst[free].next;
            lst[head].data = item;
            lst[head].next = NULL_POINTER;
            return;
        }

        if (item.compareTo(lst[head].data) < 0) {
            int temp = lst[free].next;
            lst[free].data = item;
            lst[free].next = head;
            head = free;
            free = temp;
            return;
        }

        if (item.compareTo(lst[tail].data) > 0) {
            int temp = lst[free].next;
            lst[free].data = item;
            lst[free].next = NULL_POINTER;
            lst[tail].next = free;
            tail = free;
            free = temp;
            return;
        }

        int current = head;
        while (item.compareTo(lst[lst[current].next].data) > 0) {
            current = lst[current].next;
        }

        int temp = lst[free].next;
        lst[free].data = item;
        lst[free].next = lst[current].next;
        lst[current].next = free;
        free = temp;
    }

    public static void print_list() {
        int current = head;
        while (current != NULL_POINTER) {
            System.out.print(lst[current].data + ", ");
            current = lst[current].next;
        }
    }

    public static int search_list_item(String item) {
        int current = head;
        while (current != NULL_POINTER) {
            if (lst[current].data.equals(item)) {
                return current;
            }
            current = lst[current].next;
        }
        return NULL_POINTER;
    }

    public static void print_array() {
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

    public static void delete_list_item(String item) {
        if (head == NULL_POINTER) {
            System.out.println("List is empty");
            return;
        }

        if (item.equals(lst[head].data)) {
            int temp = head;
            head = lst[head].next;
            lst[temp].next = free;
            free = temp;
            lst[free].data = "";
            return;
        }

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

        int current = head;
        while (!item.equals(lst[lst[current].next].data)) {
            current = lst[current].next;
            if (lst[current].next == NULL_POINTER) {
                System.out.println("Item not found");
                return;
            }
        }

        int temp = lst[current].next;
        lst[current].next = lst[lst[current].next].next;
        lst[temp].next = free;
        free = temp;
        lst[free].data = "";
    }

    public static void main(String[] args) {
        init_free_list();
        int option = 0;
        while (option != 6) {
            System.out.println("1. Add a node");
            System.out.println("2. Delete a node");
            System.out.println("3. Print the list");
            System.out.println("4. Print the array");
            System.out.println("5. Search an item");
            System.out.println("6. Exit");
            System.out.print("Enter your option: ");
            option = new Scanner(System.in).nextInt();
            if (option == 1) {
                System.out.print("Enter the item to be added: ");
                String item = new Scanner(System.in).nextLine();
                add_list_item(item);
            } else if (option == 2) {
                System.out.print("Enter the item to be deleted: ");
                String item = new Scanner(System.in).nextLine();
                delete_list_item(item);
            } else if (option == 3) {
                print_list();
                System.out.println();
            } else if (option == 4) {
                print_array();
            } else if (option == 5) {
                System.out.print("Enter the item to search for: ");
                String item = new Scanner(System.in).nextLine();
                int index = search_list_item(item);
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
    }
}
