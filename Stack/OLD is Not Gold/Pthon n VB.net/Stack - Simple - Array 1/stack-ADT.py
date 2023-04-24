def push(item):
    global topPointer, stackFull
    if topPointer < stackFull:
        topPointer = topPointer +1
        stack[topPointer] = item
    else:
        print("Overflow occurs, cannot PUSH.)")

def pop():
    global basePointer, topPointer
    if topPointer == basePointer -1:
        print("Underflow occurs, cannot POP.)")
        return -1
    else:
        item = stack[topPointer]
        topPointer = topPointer -1
    return item

# setup stack DS
stack = [None for index in range(0,10)]
basePointer = 0
topPointer = -1
stackFull = 9
item = None

print(stack)
push(75)
print(stack)
push(50)
print(stack)
x = pop()
print("Popped item = ", x)
print(stack)
push(25)
print(stack)