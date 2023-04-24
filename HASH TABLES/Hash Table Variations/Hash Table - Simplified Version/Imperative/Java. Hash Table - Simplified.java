import java.util.Scanner;

class SimpleHashTable {

    public static void main(String[] args) {
        // Create an array to represent the hash table.
        Integer[] hashTable = new Integer[10];

        // Insert some keys into the hash table.
        int[] keys = {45876, 32390, 95312, 64636, 23467};
        for (int key : keys) {
            insert(hashTable, key);
        }

        // Search for a key in the hash table.
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a key to search: ");
        int searchKey = scanner.nextInt();
        int foundIndex = search(hashTable, searchKey);
        if (foundIndex == -1) {
            System.out.println("Key not found.");
        } else {
            System.out.println("Key found at index " + foundIndex);
        }

        // Print the hash table.
        for (int i = 0; i < hashTable.length; i++) {
            System.out.print(hashTable[i] + " ");
        }
    }

    // Define a function to calculate the index for a given key.
    public static int hashFunction(int key, int tableSize) {
        return key % tableSize;
    }

    // Define a function to insert a key into the hash table.
    public static void insert(Integer[] hashTable, int key) {
        int index = hashFunction(key, hashTable.length);
        while (hashTable[index] != null) {
            index = (index + 1) % hashTable.length;
        }
        hashTable[index] = key;
    }

    // Define a function to search for a key in the hash table.
    public static int search(Integer[] hashTable, int key) {
        int index = hashFunction(key, hashTable.length);
        while (hashTable[index] != null && hashTable[index] != key) {
            index = (index + 1) % hashTable.length;
        }
        return hashTable[index] != null ? index : -1;
    }
}
