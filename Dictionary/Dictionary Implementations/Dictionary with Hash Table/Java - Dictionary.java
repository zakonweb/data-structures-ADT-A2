import java.util.HashMap;
import java.util.Scanner;

class Dictionary {
    private HashMap<String, String> map;

    public Dictionary() {
        map = new HashMap<>();
    }

    public void insert(String key, String value) {
        map.put(key, value);
    }

    public void delete(String key) {
        if (map.containsKey(key)) {
            map.remove(key);
        } else {
            System.out.println("Key not found!");
        }
    }

    public String search(String key) {
        return map.getOrDefault(key, "Key not found!");
    }

    public void display() {
        for (String key : map.keySet()) {
            System.out.println(key + " : " + map.get(key));
        }
    }

    public static void main(String[] args) {
        Dictionary dictionary = new Dictionary();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("\n1. Insert\n2. Delete\n3. Search\n4. Display\n5. Exit");
            int choice = scanner.nextInt();
            scanner.nextLine();
            if (choice == 1) {
                System.out.println("Enter key: ");
                String key = scanner.nextLine();
                System.out.println("Enter value: ");
                String value = scanner.nextLine();
                dictionary.insert(key, value);
            } else if (choice == 2) {
                System.out.println("Enter key: ");
                String key = scanner.nextLine();
                dictionary.delete(key);
            } else if (choice == 3) {
                System.out.println("Enter key: ");
                String key = scanner.nextLine();
                System.out.println(dictionary.search(key));
            } else if (choice == 4) {
                dictionary.display();
            } else if (choice == 5) {
                break;
            } else {
                System.out.println("Invalid choice!");
            }
        }

        scanner.close();
    }
}
