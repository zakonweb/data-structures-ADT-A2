# Simple Hash Table Implementation

This code describes an implementation of a simple hash table using open addressing (also known as linear probing) to resolve collisions.

## Hash Table

`hash_table`: A list of size 10 is declared to store the keys.

## Hash Function

`hash_function`: This function calculates the index in the hash table for a given key. It computes the remainder of the key divided by the length of the hash table.

## Insert Procedure

`insert`: This procedure inserts a key into the hash table. It first calculates the index using the `hash_function`. If the slot at the calculated index is already occupied, the procedure iterates through the hash table linearly (wrapping around to the start if necessary) until it finds an empty slot and inserts the key there.

## Search Function

`search`: This function searches for a key in the hash table. It starts by calculating the index using the `hash_function`. It then iterates through the hash table linearly (wrapping around to the start if necessary) until it finds the key or an empty slot. If the key is found, the index is returned; otherwise, NULL is returned.

## Main Program

The main program:
a. Declares a list `keys` containing five integer keys to insert into the hash table.
b. Loops through the `keys` list and inserts each key into the hash table using the `insert` procedure.
c. Reads an integer `search_key` from the user to search for in the hash table.
d. Calls the `search` function with `search_key` and stores the result in `found_index`.
e. If `found_index` is NULL, it means the key was not found; otherwise, the key was found at the specified index.
f. Loops through the `hash_table` list and prints its content.

# Summary

In summary, this pseudocode provides a simple way to implement a hash table with open addressing (linear probing) for resolving collisions. It demonstrates how to insert keys into the hash table, search for a specific key, and print the hash table's content.
