# Ordered Linked List

This is a Python implementation of an ordered linked list, a data structure that maintains a sorted list of elements. Each element in the list is represented by a node, and these nodes are organized in ascending order based on their values. This README explains how the ordered linked list works and provides an overview of each function and class.

## Table of Contents
- [Introduction](#introduction)
- [Node Class](#node-class)
- [OrderedLinkedList Class](#orderedlinkedlist-class)
  - [Inserting an Item](#inserting-an-item)
  - [Removing an Item](#removing-an-item)
  - [Searching for an Item](#searching-for-an-item)
  - [String Representation](#string-representation)
- [Usage](#usage)

## Introduction

A linked list is a linear data structure that stores a collection of items. Unlike an array, it does not provide constant-time access to specific elements by index. Instead, it requires iterating through the list to find the desired element. The advantage of a linked list is that it allows for efficient insertion and removal of elements at the beginning of the list.

An ordered linked list is a variation of a linked list that maintains its elements in sorted order. When you insert a new element, it is placed in its correct position to preserve the ordering. Similarly, when you delete an element, it is removed from its correct position.

## Node Class

The `Node` class represents a single node in the linked list. Each node contains two attributes:
- `data`: Stores the item value.
- `next`: Points to the next node in the list.

## OrderedLinkedList Class

The `OrderedLinkedList` class is the data structure that manages the ordered linked list. It contains the following methods:

### Inserting an Item

```python
def insert_item(self, item: int) -> None:
```

This method inserts a new node with the given integer item into the linked list while maintaining the sorted order. It iterates through the list to find the correct position for insertion, ensuring that the list remains ordered.

### Removing an Item

```python
def remove_item(self, item: int) -> None:
```

This method removes the first occurrence of the specified integer `item`` from the linked list.

### Searching for an Item

```python
def search_item(self, item: int) -> int:
```

This method searches for a specific integer `item` in the linked list and returns its index if found; otherwise, it returns -1.

### String Representation
The `OrderedLinkedList` class also provides string representation methods:

- ```__str__(self)```: Returns a string representation of the linked list by iterating through each node and appending their data to the output string.

- ```__repr__(self)```: Returns a string representation of the linked list by creating a list of node data and joining them with commas.

## Usage
To use the ordered linked list, create an instance of `OrderedLinkedList`, and then interact with it using the provided operations:

- Add a node: `insert_item(item)`
- Delete a node: `remove_item(item)`
- Print the list: `print(li)`
- Search for an item: `search_item(item)`
- Here is an example menu-driven program that demonstrates the usage:

```python
li = OrderedLinkedList()
option = 0

while option != 6:
    print("Ordered Linked List Operations")
    print('1. Add a node')
    print('2. Delete a node')
    print('3. Print the list')
    print('5. Search an item')
    print('6. Exit')

    option = int(input('Enter your option: '))

    if option == 1:
        item = int(input('Enter the item to be added: '))
        li.insert_item(item)

    elif option == 2:
        item = int(input('Enter the item to be deleted: '))
        li.remove_item(item)

    elif option == 3:
        print(li)

    elif option == 5:
        item = int(input('Enter the item to search for: '))
        index = li.search_item(item)

        if index == -1:
            print("Item not found.")
        else:
            print("Item found at index", index)

    elif option == 6:
        print('Goodbye!')
    else:
        print('Invalid option')
```