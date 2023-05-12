# Create a list to represent the hash table.
hash_table = [None] * 10

# Define a function to calculate the index for a given key.
def hash_function(key):
    return key % len(hash_table)

# Define a function to insert a key into the hash table.
def insert(key):
    index = hash_function(key)
    while hash_table[index] is not None:
        index = (index + 1) % len(hash_table)
    hash_table[index] = key

# Define a function to search for a key in the hash table.
def search(key):
    index = hash_function(key)
    while hash_table[index] != key:
        index = (index + 1) % len(hash_table)
        if hash_table[index] is None:
            return None
    return index

# Insert some keys into the hash table.
keys = [45876, 32390, 95312, 64636, 23467]
for key in keys:
    insert(key)

# Search for a key in the hash table.
search_key = int(input("Enter a key to search: "))
found_index = search(search_key)
if found_index is None:
    print("Key not found.")
else:
    print(f"Key found at index {found_index}")

# Print the hash table.
print(hash_table)
