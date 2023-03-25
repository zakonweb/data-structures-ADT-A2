# Set up constants and variables
NULL_POINTER = -1
Stack = []
TopOfStack = NULL_POINTER

# Define subroutine for pushing a value onto the stack
def push(value):
    """ Receives a value as parameter from user and pushes it onto the stack """
    global Stack, TopOfStack
    if TopOfStack == len(Stack) - 1:
        # Stack is full
        print("Stack is full. Cannot push value.")
    else:
        # Increment TopOfStack and add the value to the Stack
        TopOfStack += 1
        Stack[TopOfStack] = value

# Define subroutine for popping the top element from the stack
def pop():
    """ Removes the top element from the stack and returns it """
    global Stack, TopOfStack
    if TopOfStack == NULL_POINTER:
        # Stack is empty
        print("Stack is empty. Cannot pop value.")
    else:
        # Get the top value from the stack, decrement TopOfStack, and return the value
        value = Stack[TopOfStack]
        TopOfStack -= 1
        return value

# Define subroutine for displaying the stack as a list of values with the pointer at the top
def display():
    """visialize the stack elements line by line and shows pointer value first"""
    global Stack, TopOfStack
    if TopOfStack == NULL_POINTER:
        # Stack is empty
        print("Stack is empty. Cannot display value.")
    else:
        # Print the pointer value and the stack elements in reverse order
        print("Pointer is at", TopOfStack)
        for i in range(TopOfStack, NULL_POINTER, -1):
            print(Stack[i])

# Define subroutine for displaying the entire stack array with the pointer value
def display_array():
    """displays the array elements, their index and the pointer value"""
    global Stack, TopOfStack
    if TopOfStack == NULL_POINTER:
        # Stack is empty
        print("Stack is empty. Cannot display value.")
    else:
        # Print the pointer value and the entire stack array
        print("Pointer is at", TopOfStack)
        for i in range(len(Stack)):
            print("Index", i, ":", Stack[i])

# Main program
# Ask the user for the size of the stack
size = int(input("Enter the size of the stack: "))

# Initialize the stack array with None values and start the menu loop
Stack = [None] * size
while True:
    # Print the menu options
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Display Array")
    print("5. Exit")

    # Ask the user for their choice and perform the selected operation
    choice = int(input("Enter your choice: "))
    if choice == 1:
        # Push a value onto the stack
        value = int(input("Enter the value to push: "))
        push(value)
    elif choice == 2:
        # Pop the top value from the stack
        value = pop()
        if value is not None:
            print("Popped value is", value)
    elif choice == 3:
        # Display the stack as a list of values with the pointer at the top
        display()
    elif choice == 4:
        # Display the entire stack array with the pointer value
        display_array()
    elif choice == 5:
        # Exit the program
        break
    else:
        # Invalid choice, ask the user to try again
        print("Invalid choice. Try again.")
