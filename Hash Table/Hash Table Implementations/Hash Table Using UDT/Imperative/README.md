# Hash Table Implementation

This code represents an implementation of a hash table data structure, a common data structure in computer science utilized for storing key-value pairs for efficient insertion and retrieval of values.

## Code Components

### RECORD User-Defined Type (UDT)

The code begins by defining a `RECORD` user-defined type (UDT) with two fields, `key` and `value`. These represent the key-value pairs stored in the hash table.

### HashFunction()

The `HashFunction()` takes a key and a size parameter, returning an integer hash code based on the key value and the size of the hash table.

### SearchHash()

The `SearchHash()` function takes a `recordKey` and a `hashTable[]` parameter. It searches the hash table for a record with the provided `recordKey`. If found, it returns the index of the record in the hash table, otherwise, it returns `-1`.

### InsertHash()

The `InsertHash()` procedure takes a record and a `hashTable[]` parameter. It inserts the record into the hash table using the hash function to determine the index at which to insert the record.

## MAIN Code Block

The `MAIN` code block works as follows:

1. **Record Input:** It prompts the user to input 11 record keys and inserts them into the hash table using the `InsertHash()` procedure.
2. **Search:** The user is then prompted to enter a search key. The program searches the hash table for a record with that key using the `SearchHash()` function.
3. **Output:** If the record is found, the code prints the corresponding value; if not, it prints "Not Found".
4. **Display:** The code then prints out the values of all the records in the hash table using a `FOR...NEXT` loop, and waits for the user to press a key before exiting the program.
