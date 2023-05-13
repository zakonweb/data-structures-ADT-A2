# Stack Data Structure Implementation using a Linked List

This program implements a **stack data structure using a linked list**. The stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle, where the last element added to the stack is the first element to be removed.

## Data Structure and Global Pointers

This implementation uses an array of Node structures to store the elements in the stack. Each Node structure contains an Integer data and a 'next' pointer that holds the index of the next Node in the stack. A linked list is used to maintain the order of the elements within the stack, and global pointers (top_of_stack, head, free) are used to manage the stack and linked list.

## Program Functionalities

The program provides the following functionalities:

1. Initialize the stack.
2. Push an element onto the stack.
3. Pop an element from the stack.
4. Display the stack.
5. Display the array containing the linked list nodes.

## Stack Operations

The program defines several functions for performing stack operations:

### `InitializeStack()`

Initializes the stack by setting the global pointers to their initial values and linking the free nodes together.

### `Push(data)`

Pushes an element (data) onto the stack. If there's no free node available, it prints "Stack Overflow" and returns without pushing the data.

### `Pop()`

Pops an element from the top of the stack and returns it. If the stack is empty, it prints "Stack Underflow" and returns Nothing (a nullable integer).

### `DisplayStack()`

Displays the current elements in the stack, starting from the top.

### `DisplayArray()`

Displays the array containing the linked list nodes, their data, and their 'next' pointers, along with the current values of the global pointers.

## Main Function and User Interaction

The `Main()` function provides an interactive menu for the user to perform stack operations. It runs in a loop, allowing the user to choose an option until they decide to exit (option 5). The menu options are:

1. Push: Prompts the user to enter an integer value and pushes it onto the stack.
2. Pop: Pops an element from the stack and displays it if there was a valid value.
3. Display Stack: Displays the current elements in the stack.
4. Print Linked List Array: Displays the array containing the linked list nodes, their data, and their 'next' pointers, along with the current values of the global pointers.
5. Exit: Exits the program.

When the user chooses an option, the appropriate function is called to perform the selected operation. The `Main()` function continues to run in a loop until the user chooses the "Exit" option.
