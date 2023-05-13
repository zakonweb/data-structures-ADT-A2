# Hash Table with Insert and Search Operations

This code demonstrates a hash table that allows a user to insert and search for a record key in the hash table. Here's a more detailed explanation:

## Initialization

The main program begins by initializing an array named `hashTable` with 10 elements.

## Insertion

The program prompts the user to enter 10 record keys by iterating through a `For` loop. The loop reads the record key from the user and inserts it into the hash table using the `InsertHash` subroutine.

`InsertHash` subroutine calculates the index of the key using the `HashFunction` and places the key into the hash table at the calculated index. If the index is already occupied, the subroutine finds the next available index.

## Search

After the insertion of keys, the main program prompts the user to input a search record key. The program then searches for this key in the hash table using the `SearchHash` function. 

The `SearchHash` function calculates the index of the key using the `HashFunction`. If the key is found, the function returns the index of the key. If the key is not found, it returns -1.

## Output

Finally, the main program outputs whether the key was found or not, along with the contents of the hash table using another `For` loop.
