def push():
    global topofstackpointer, fullstack, stack
    value = 0
    if topofstackpointer == fullstack:
        print("Overflow, Stack is full. No more value can be added.")
    else:
        value = int(input("Enter value to add to stack: "))
        topofstackpointer +=1
        stack[topofstackpointer] = value
        return

def pop():
    global topofstackpointer, nullpointer, stack
    if topofstackpointer == nullpointer:
        value = nullpointer
    else:
        value = stack[topofstackpointer]
        topofstackpointer -=1
    return value

stack = []
fullstack = 8
baseofstackpointer = 0
topofstackpointer = -1
nullpointer = -1
choice = 0
for i in range(8):
    stack.append("")

while not choice == 3:
    print("1. Push to stack.\n2. Pop from stack.\n3. Exit program.")
    choice = int(input("Enter your choice 1..3 : "))

    if choice == 1:
        push()
    elif choice == 2:
        value = pop()
        if value == -1:
            print("Underflow, Stack is empty. No value to pop")
        else:
            print("Stack Value poped :", value)
