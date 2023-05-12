# Understanding Hash Tables

Hash tables are a powerful data structure used to store and retrieve data efficiently. They provide fast access to data items by using a technique called hashing. In this guide, we'll explore the concept of hash tables and how they work.

## Anatomy of a Hash Table

A hash table consists of two main components: an array and a hash function.

### Array

The array is a collection of "buckets" or "slots" where data items are stored. Each bucket has a unique index or position within the array.

### Hash Function

The hash function is a crucial part of a hash table. It takes the data item as input and calculates a unique numeric value called the "hash code" or "hash value". The hash code is used to determine the index of the bucket where the data item will be stored in the array.

## Hashing Process

The hashing process involves two main steps: hashing and collision resolution.

### Hashing

1. The hash function takes the data item and calculates its hash code.
2. The hash code is then mapped to a valid index within the array using a technique called modulo division. This ensures that the index falls within the bounds of the array size.

### Collision Resolution

Collisions occur when two different data items produce the same hash code and attempt to occupy the same index in the array. Hash tables use various collision resolution techniques to handle these situations. Two commonly used methods are:

1. **Chaining**: Each bucket in the array contains a linked list. If a collision occurs, the new data item is appended to the linked list at the corresponding bucket index.
2. **Open Addressing**: When a collision occurs, a new index is calculated by applying an additional computation to the original hash code. The new index is determined using techniques such as linear probing (checking the next available index), quadratic probing (checking indices based on a quadratic function), or double hashing (using a secondary hash function).

## Hash Table Operations

### Insertion

To insert a data item into a hash table, we follow these steps:

1. Calculate the hash code for the data item.
2. Use the hash code to determine the index where the data item should be stored in the array.
3. If no collision occurs, store the data item at the determined index.
4. If a collision occurs, use the collision resolution technique (e.g., chaining or open addressing) to handle it.

### Searching

To search for a data item in a hash table, we perform the following steps:

1. Calculate the hash code for the target data item.
2. Use the hash code to determine the index where the data item should be located.
3. If the data item is found at the determined index, return it.
4. If a collision occurred and the data item is stored in a linked list or a different index, search the appropriate data structure (linked list or check the next indices) to find the item.

### Deletion

To delete a data item from a hash table, we perform the following steps:

1. Calculate the hash code for the target data item.
2. Use the hash code to determine the index where the data item should be located.
3. If the data item is found at the determined index, remove it.
4. If a collision occurred and the data item is stored in a linked list or a different index, search the appropriate data structure and remove the item.

## Summary

Hash tables provide efficient storage and retrieval of data by leveraging the power of hashing. They are widely used to solve a variety of real-world problems, including fast data lookup, caching, and database indexing. Understanding hash
