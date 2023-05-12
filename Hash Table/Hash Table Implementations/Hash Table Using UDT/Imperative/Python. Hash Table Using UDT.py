class Record:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size

    def hash_function(self, key):
        return key % (self.size + 1)

    def insert(self, new_record):
        index = self.hash_function(new_record.key)
        while self.table[index] is not None:
            index += 1
            if index > self.size - 1:
                index = 0
        self.table[index] = new_record

    def find_record(self, search_key):
        index = self.hash_function(search_key)
        while (self.table[index] is not None) and (self.table[index].key != search_key):
            index += 1
            if index > self.size - 1:
                index = 0
        if self.table[index] is not None:
            return self.table[index]
        else:
            return None

    def __str__(self):
        return str([str(record.value) if record else None for record in self.table])


def main():
    hash_table = HashTable(9)
    record_keys = [45876, 32390, 95312, 64636, 23467]

    for key in record_keys:
        record = Record(key, f"Customer {key}")
        hash_table.insert(record)

    search_key = int(input("Enter Search Record Key: "))
    record = hash_table.find_record(search_key)
    if record is None:
        print("Not Found")
    else:
        print(f"Found: {record.value}")

    print(hash_table)


if __name__ == "__main__":
    main()
