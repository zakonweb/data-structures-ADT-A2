# Unordered Linked List

This is a Python implementation of an unordered linked list, a data structure that stores a list of elements without any specific order. Each element in the list is represented by a node, and these nodes are connected together. This README explains how the unordered linked list works and provides an overview of each function and class.

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

An unordered linked list is a simple variation of a linked list that does not maintain any specific order for its elements. When you insert a new element, it is simply added to the end of the list. Similarly, when you delete an element, it is removed from the list without any regard for its position.

## Node Class

The `Node` class represents a single node in the linked list. Each node contains two attributes:
- `data`: Stores the item value.
- `next`: Points to the next node in the list.

## LinkedList Class

The `LinkedList` class is the data structure that manages the unordered linked list. It contains the following methods:

### Inserting an Item

```python
def insert_item(self, item: int) -> None:
```

This method inserts a new node with the given integer item into the linked list. The new node is added to the beginning of the list, and its position is not determined by the item value.

### Removing an Item

```python
def remove_item(self) -> None:
```

The function removes the first item from the linked list. It does not take a specific item as input and remove it based on its value. Instead, it removes the first item encountered in the linked list

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
To use the unordered linked list, create an instance of `LinkedList`, and then interact with it using the provided operations:

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