def insert_hash(record_key, hash_table):
    """Insert the record key into the hash table."""
    index = hash_function(record_key, len(hash_table) - 1)
    while hash_table[index] != 0:
        index += 1
        if index > len(hash_table) - 1:
            index = 0
    hash_table[index] = record_key


def search_hash(record_key, hash_table):
    """Search for the record key in the hash table and return its index, or -1 if not found."""
    total_searches = 0
    index = hash_function(record_key, len(hash_table) - 1)
    while hash_table[index] != record_key:
        total_searches += 1
        index += 1
        if index > len(hash_table) - 1:
            index = 0
        if total_searches > len(hash_table) - 1:
            return -1
    return index


def hash_function(key_value, max_position):
    """Calculate the index position for a given key value."""
    return key_value % (max_position + 1)


def main():
    hash_table = [0] * 11

    for _ in range(11):
        record_key = int(input("Enter Record Key: "))
        insert_hash(record_key, hash_table)

    search_record_key = int(input("Enter Search Record Key: "))
    found_index = search_hash(search_record_key, hash_table)
    if found_index == -1:
        print("Not Found")
    else:
        print("Found")

    for item in hash_table:
        print(item)


if __name__ == "__main__":
    main()
