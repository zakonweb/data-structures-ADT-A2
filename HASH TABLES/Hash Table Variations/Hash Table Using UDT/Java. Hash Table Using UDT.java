import java.util.Scanner;

class HashTableExample {

    public static void main(String[] args) {
        HashTable hashTable = new HashTable(9);
        int[] recordKeys = {45876, 32390, 95312, 64636, 23467};

        for (int key : recordKeys) {
            Record record = new Record(key, "Customer " + key);
            hashTable.insert(record);
        }

        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter Search Record Key: ");
        int searchKey = scanner.nextInt();
        Record record = hashTable.findRecord(searchKey);
        if (record == null) {
            System.out.println("Not Found");
        } else {
            System.out.println("Found: " + record.value);
        }

        System.out.println(hashTable);
    }

    public static class Record {
        public int key;
        public String value;

        public Record(int key, String value) {
            this.key = key;
            this.value = value;
        }
    }

    public static class HashTable {
        private int size;
        private Record[] table;

        public HashTable(int size) {
            this.size = size;
            this.table = new Record[size];
        }

        public int hashFunction(int key) {
            return key % (size + 1);
        }

        public void insert(Record newRecord) {
            int index = hashFunction(newRecord.key);
            while (table[index] != null) {
                index++;
                if (index > size - 1) {
                    index = 0;
                }
            }
            table[index] = newRecord;
        }

        public Record findRecord(int searchKey) {
            int index = hashFunction(searchKey);
            while ((table[index] != null) && (table[index].key != searchKey)) {
                index++;
                if (index > size - 1) {
                    index = 0;
                }
            }
            if (table[index] != null) {
                return table[index];
            } else {
                return null;
            }
        }

        public String toString() {
            String result = "[";
            for (Record record : table) {
                if (record != null) {
                    result += record.value;
                } else {
                    result += "null";
                }
                result += ", ";
            }
            result = result.substring(0, result.length() - 2);
            result += "]";
            return result;
        }
    }
}
