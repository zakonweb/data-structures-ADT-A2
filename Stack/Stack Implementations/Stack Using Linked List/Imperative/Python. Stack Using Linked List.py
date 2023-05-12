"""
Python code to implement stack using linked list.
It uses the concept of LIFO (Last In First Out).
It has following global pointers: top_of_stack, head, free.
It has following functions: push, pop, display_array, display_stack.
"""
# Linked List Node
class Node:
    def __init__(self):
        self.data = None
        self.next = -1

# constant 
MAX = 10
NULL_POINTER = -1

# global variables
top_of_stack = NULL_POINTER
head = NULL_POINTER
free = 0

# stack array of nodes
stack = [Node() for i in range(MAX)]

# function to initialize the stack
def initialize_stack():
    global top_of_stack, head, free
    top_of_stack = NULL_POINTER
    head = NULL_POINTER
    free = 0
    for i in range(MAX - 1):
        stack[i].next = i + 1
    stack[MAX - 1].next = NULL_POINTER

# function to push an element into the stack
def push(data):
    global top_of_stack, head, free
    if free == NULL_POINTER:
        print("Stack Overflow")
        return
    else:
        temp = free
        free = stack[free].next
        stack[temp].data = data 
        stack[temp].next = top_of_stack
        top_of_stack = temp
        if head == NULL_POINTER:
            head = top_of_stack

# function to pop an element from the stack
def pop():
    global top_of_stack, head, free
    if top_of_stack == NULL_POINTER:
        print("Stack Underflow")
        return False
    else:
        temp = top_of_stack
        top_of_stack = stack[top_of_stack].next
        stack[temp].next = free
        free = temp
        if top_of_stack == NULL_POINTER:
            head = NULL_POINTER
        val = stack[temp].data
        stack[temp].data = None
        return val

# function to display the stack
def display_stack():
    global top_of_stack, head, free
    if top_of_stack == NULL_POINTER:
        print("Stack is Empty")
        return
    else:
        temp = top_of_stack
        while temp != NULL_POINTER:
            if temp == top_of_stack:
                print(stack[temp].data, "←")
            else:
                print(stack[temp].data)
            temp = stack[temp].next

# function to display the array
def display_array():
    global top_of_stack, head, free
    print("index\tdata\tnext")
    for i in range(MAX):
        print(f"{i}\t{stack[i].data}\t{stack[i].next}", end="")
        if i == free:
            print("\tfree")
        elif i == top_of_stack:
            print("\ttop_of_stack | tail_of_LL")
        elif i == head:
            print("\thead")
        else:
            print()
    print("top_of_stack: ", top_of_stack)
    print("head: ", head)
    print("free: ", free)

# main program
initialize_stack()
option = 0

while option != 5:
    print("\nStack Using Linked List")    
    print("1. Push")
    print("2. Pop")
    print("3. Display Stack")
    print("4. Print Linked List Array")
    print("5. Exit")
    option = int(input("Enter your choice: "))
    if option == 1:
        data = int(input("Enter integer data: "))
        push(data)
    elif option == 2:
        data = pop()
        if data != False:
            print("Popped element: ", data)
    elif option == 3:
        display_stack()
    elif option == 4:
        display_array()
    elif option == 5:
        print("Thank You")
    else:
        print("Invalid Choice")
# end of program