# Stack Data Structure Implementation using an Array

This code is a simple program to **implement a stack data structure using an array**. It allows the user to perform various operations on the stack, like pushing and popping values, as well as displaying the stack and the array used to store its values.

## Variables Declaration

Three variables are declared: 
1. `NULL_POINTER` (a constant to represent an empty stack)
2. `STACK` (the array used to store the stack values)
3. `TOP_OF_STACK` (an integer to keep track of the top element's position in the stack).

The user is prompted to enter the desired size of the stack, and then the stack array is initialized with null values.

## Subroutines

Four subroutines (procedures) are defined to perform operations on the stack:

### `PUSH()`

Prompts the user for a value and adds (pushes) it onto the top of the stack, unless the stack is full.

### `POP()`

Removes (pops) the top value from the stack and displays it, unless the stack is empty.

### `DISPLAY()`

Displays the current stack as a list of values with the pointer at the top, unless the stack is empty.

### `DISPLAY_ARRAY()`

Displays the entire stack array along with the pointer value, unless the stack is empty.

## Main Program Loop

The program enters a loop (menu loop), where it displays a menu with five options for the user to choose from:

1. Push - Calls the `PUSH()` subroutine.
2. Pop - Calls the `POP()` subroutine.
3. Display - Calls the `DISPLAY()` subroutine.
4. Display Array - Calls the `DISPLAY_ARRAY()` subroutine.
5. Exit - Exits the program.

Based on the user's choice, the program calls the appropriate subroutine. If the user enters an invalid choice, the program displays an error message and prompts the user to try again. The menu loop continues until the user chooses to exit the program.
