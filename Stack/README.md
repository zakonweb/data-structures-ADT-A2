# Understanding Stacks

Stacks are a fundamental data structure that follows the **Last-In-First-Out** (LIFO) principle. They are commonly used to manage data in a sequential manner. In this guide, we'll explore the concept of stacks, their operations, and how they work.

## Anatomy of a Stack

A stack is a collection of elements that supports two main operations: **push** and **pop**. The push operation adds an element to the top of the stack, while the pop operation removes the topmost element from the stack.

![Stack Anatomy](https://cdn.programiz.com/sites/tutorial2program/files/stack.png)

## Stack Operations

The Stack ADT supports the following fundamental operations:

### Push (Addition)

To add an element to the stack, we perform the push operation. It involves the following steps:

1. Check if the stack is full (if it has reached its maximum capacity).
2. If the stack is full, display an overflow message and stop.
3. If the stack is not full, increment the top pointer and add the new element at that position.

### Pop (Removal)

To remove an element from the stack, we perform the pop operation. It involves the following steps:

1. Check if the stack is empty (if there are no elements).
2. If the stack is empty, display an underflow message and stop.
3. If the stack is not empty, remove the element from the top (by decrementing the top pointer) and return the removed element.

## Stack Implementations

There are different ways to implement a stack. Two common implementations are:

### Array-based Stack

In this implementation, a fixed-size array or a dynamic array is used to store the elements of the stack. The top pointer keeps track of the index of the top element in the array. Elements are pushed onto the stack by incrementing the top pointer and placing the new element at that position. Elements are popped from the stack by removing the element at the top pointer and decrementing the top pointer.

![Array-based Stack](https://media.geeksforgeeks.org/wp-content/uploads/20210409185210/HowtoImplementStackinJavaUsingArrayandGenerics.jpg)

### Linked List-based Stack

In this implementation, a dynamic linked list is used to represent the stack. Each node in the linked list contains the element and a pointer to the next node. The top pointer points to the first node of the linked list. Elements are pushed onto the stack by creating a new node and updating the top pointer to point to the new node. Elements are popped from the stack by removing the first node and updating the top pointer to point to the next node.

![Linked List-based Stack](http://www.btechsmartclass.com/data_structures/ds_images/stack_implementation_using_linked_list.png)

## Summary

Stacks are a simple yet powerful data structure that follows the Last-In-First-Out principle
