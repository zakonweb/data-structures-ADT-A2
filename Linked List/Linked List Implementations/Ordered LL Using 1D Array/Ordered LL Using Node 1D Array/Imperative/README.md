# Linked List Implementation using Two Parallel Arrays

This code creates an ordered linked list using an array named `lst[]`. The linked list is ordered in ascending order based on the `data` attribute of each node. The list can store a maximum of 10 nodes. The list uses three pointers: `head`, `tail`, and `free` to manage the nodes.

## Overview of the components:

- **NULL_POINTER**: A constant (-1) is defined to represent a null pointer. It is used to identify the end of the list and the absence of a connection between nodes.

- **node structure**: A structure for nodes is defined, with each node containing two attributes: `data` and `next`. `data` stores the actual data, and `next` stores the index of the next node in the `lst[]` array.

- **Global pointers**: `head`, `tail`, and `free` are declared as global pointers. `head` points to the first node in the list, `tail` points to the last node, and `free` points to the first available free node.

- **lst**: An array of 10 nodes is created, with each node initialized using the node structure.

## Functions:

- **init_free_list()**: This function initializes the list by setting the `head` and `tail` pointers to `NULL_POINTER` and connecting all nodes in the `lst[]` array to create a free list.

- **add_list_item(item)**: This function inserts a new item into the list while maintaining the order. It first checks if there are any available nodes. If the list is full, it prints a message and returns. Then, it checks if the item should be added at the `head`, `tail`, or in the middle of the list, and inserts it accordingly.

- **print_list()**: This function iterates through the list and prints the `data` attribute of each node.

- **search_list_item(item)**: This function searches for a specific item in the list. If the item is found, it returns the index of the item in the `lst[]` array. If not found, it returns `NULL_POINTER`.

- **print_array()**: This function prints the entire `lst[]` array along with the related pointers (`head`, `tail`, and `free`).

- **delete_list_item(item)**: This function removes a specific item from the list. It first checks if the item is at the `head`, `tail`, or in the middle of the list, and then deletes it accordingly.

## Main Program:

The main program is a loop that allows users to interact with the list. Users can add nodes, delete nodes, print the list, print the array, search for an item, or exit the program by selecting the corresponding option.

In summary, this code implements an ordered linked list using an array of fixed size. The list allows users to add, delete, and search items while maintaining the order of the elements. The code also provides functions to print the list and the underlying array structure for debugging purposes.
