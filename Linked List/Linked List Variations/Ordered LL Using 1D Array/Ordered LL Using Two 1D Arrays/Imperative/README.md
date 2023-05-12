# Linked List Using Two Parallel Arrays: A Beginner's Guide

This tutorial provides an introduction to the concept of an ordered linked list, implemented using pseudocode. We will use two parallel one-dimensional arrays instead of a typical node-based structure. 

## What is a Linked List?

A linked list is a dynamic data structure where each element (known as a node) contains a value and a reference (link) to the next node in the sequence. 

## What are we doing differently?

Instead of using a typical node structure, which combines data and the 'next' pointer in one unit, we're going to use two separate arrays: 

1. `data` array: This will hold the actual data of our nodes.
2. `next` array: This will hold the index of the next node in the list. 

We also use three pointers - `head`, `tail`, and `free` - to keep track of the start of the list, the end of the list, and any unallocated nodes, respectively.

## How does it work?

### Initialization

First, we initialize our list with the `init_free_list` procedure. This sets up a "free list" - a list of nodes that are currently unallocated and can be used to store data.

### Adding Nodes

To add a node, we use the `add_list_item` procedure. This adds a node to the list in ascending order. The procedure checks if there is a free node available, and if so, it assigns the data to the node and adjusts the pointers accordingly. It also takes care of special cases, such as when the list is empty or when the item to be added is smaller or larger than all existing items.

### Deleting Nodes

The `delete_list_item` procedure is used to remove a node from the list. It takes care of different scenarios - when the item to be deleted is at the head, tail, or in the middle of the list.

### Other Functions

- `print_list` procedure traverses the list from the head to the tail, printing out the data in each node.
- `print_array` procedure prints the current state of the `data` and `next` arrays, as well as the `head`, `tail`, and `free` pointers.
- `search_list_item` function searches for an item in the list and returns its index if found.

## The Main Loop

The main part of the pseudocode is a loop that allows the user to interact with the list, adding or deleting nodes, printing the list or array, and searching for items.

We hope this tutorial provides a good starting point for understanding how linked lists can be implemented using two parallel arrays. Remember, the key is to keep track of the data and the 'next' pointers separately, and to always update your pointers when you add or delete nodes. Happy coding!

# Advanced Operations

## Adding Nodes in Sorted Order

What makes this linked list unique is that nodes are added in a sorted fashion. This means, if you try to add a value, it won't just be added at the end of the list, but rather, it will be inserted in the correct position that maintains the sorted order of the list.

To do this, the `add_list_item` procedure goes through the following steps:

1. Checks if the list is full. If so, it doesn't add the item and exits.
2. If the list is empty, the new item becomes the head (and tail) of the list.
3. If the new item is less than the current head, it becomes the new head.
4. If the new item is more than the current tail, it becomes the new tail.
5. If none of the above, the procedure finds the correct position for the new item and inserts it there.

## Deleting Nodes

The `delete_list_item` procedure handles the deletion of nodes from the list. The procedure considers different scenarios:

1. If the list is empty, it notifies the user and exits.
2. If the node to be deleted is at the head, it moves the head pointer to the next node.
3. If the node to be deleted is at the tail, it moves the tail pointer to the previous node.
4. If the node to be deleted is in the middle, it adjusts the 'next' pointer of the previous node to point to the next node.
5. After deletion, the procedure returns the node to the free list by updating the 'next' pointer of the deleted node and the `free` pointer.

## Searching Nodes

The `search_list_item` function lets you search for a value in the list. It starts at the head and traverses the list until it finds the item or reaches the end of the list. If the item is found, it returns the index of the item. If not, it returns a `NULL_POINTER`.

## Printing Nodes

There are two printing functions: `print_list` and `print_array`. 

1. `print_list` prints all the nodes in the list in order, starting from the head.
2. `print_array` provides a more detailed view, showing the current state of the `data` and `next` arrays, as well as the `head`, `tail`, and `free` pointers.

## Wrapping Up

This pseudocode provides a comprehensive guide to implementing a sorted linked list using two parallel arrays. It covers all the essential operations, including initialization, adding, deleting, searching, and printing nodes. Understanding this will give you a solid foundation for implementing and working with linked lists.

Remember to always keep track of your pointers when you add or delete nodes. This is crucial for maintaining the integrity of the list. Now you're ready to dive deeper into data structures and algorithms. Happy coding!
