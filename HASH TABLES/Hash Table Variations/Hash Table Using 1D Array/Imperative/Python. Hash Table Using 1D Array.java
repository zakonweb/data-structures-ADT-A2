import java.util.Scanner;

class HashTableExample {

    public static void main(String[] args) {
        int[] hashTable = new int[11];

        Scanner scanner = new Scanner(System.in);
        for (int i = 0; i < 11; i++) {
            System.out.print("Enter Record Key: ");
            int recordKey = scanner.nextInt();
            insertHash(recordKey, hashTable);
        }

        System.out.print("Enter Search Record Key: ");
        int searchRecordKey = scanner.nextInt();
        int foundIndex = searchHash(searchRecordKey, hashTable);
        if (foundIndex == -1) {
            System.out.println("Not Found");
        } else {
            System.out.println("Found");
        }

        for (int item : hashTable) {
            System.out.println(item);
        }
    }

    public static void insertHash(int recordKey, int[] hashTable) {
        int index = hashFunction(recordKey, hashTable.length - 1);
        while (hashTable[index] != 0) {
            index++;
            if (index > hashTable.length - 1) {
                index = 0;
            }
        }
        hashTable[index] = recordKey;
    }

    public static int searchHash(int recordKey, int[] hashTable) {
        int totalSearches = 0;
        int index = hashFunction(recordKey, hashTable.length - 1);
        while (hashTable[index] != recordKey) {
            totalSearches++;
            index++;
            if (index > hashTable.length - 1) {
                index = 0;
            }
            if (totalSearches > hashTable.length - 1) {
                return -1;
            }
        }
        return index;
    }

    public static int hashFunction(int keyValue, int maxPosition) {
        return keyValue % (maxPosition + 1);
    }
}
