NULLPOINTER = -1
CurrentNodePtr = TopOfStack = FreeListPtr = 0
Stack = []


def GetOption():
    print("1: Push a value\n2: Pop a value\n3: Output Stack\n4: End Program")
    choice = int(input("Enter your choice: "))
    return choice


def InitialiseStack():
    global NULLPOINTER, TopOfStack, FreeListPtr, Stack
    TopOfStack = NULLPOINTER
    FreeListPtr = 0
    for Index in range(8):
        Stack.append(Node("", Index + 1))
    Stack[7].Pointer = NULLPOINTER

def Pop():
    global TopOfStack, NULLPOINTER, Stack, FreeListPtr
    if TopOfStack == NULLPOINTER:
        print("no data on stack")
        Value = ""
    else:
        Value = Stack[TopOfStack].Data
        ThisNodePtr = TopOfStack
        TopOfStack = Stack[TopOfStack].Pointer
        Stack[ThisNodePtr].Pointer = FreeListPtr
        FreeListPtr = ThisNodePtr
    return Value


def Push(NewItem):
    global NULLPOINTER, TopOfStack, FreeListPtr, Stack
    if FreeListPtr != NULLPOINTER:
        NewNodePtr = FreeListPtr
        Stack[NewNodePtr].Data = NewItem
        FreeListPtr = Stack[FreeListPtr].Pointer
        Stack[NewNodePtr].Pointer = TopOfStack
        TopOfStack = NewNodePtr
    else:
        print("no space for more data")


def OutputAllNodes():
    global NULLPOINTER, TopOfStack, FreeListPtr, Stack
    CurrentNodePtr = TopOfStack
    if TopOfStack == NULLPOINTER:
        print("no data on stack")
    while CurrentNodePtr != NULLPOINTER:
        print(CurrentNodePtr, Stack[CurrentNodePtr].Data)
        CurrentNodePtr = Stack[CurrentNodePtr].Pointer


class Node:
    def __init__(self, Data, Pointer):
        self.Data = Data
        self.Pointer = Pointer


InitialiseStack()
Choice = GetOption()
while Choice != 4:
    if Choice == 1:
        Data = input("Enter the value: ")
        Push(Data)
        OutputAllNodes()
    if Choice == 2:
        Data = Pop()
        print("Data popped:", Data)
    if Choice == 3:
        OutputAllNodes()
        print(TopOfStack, FreeListPtr)
        for i in range(7):
            print(i, Stack[i].Data, Stack[i].Pointer)
    Choice = GetOption()
