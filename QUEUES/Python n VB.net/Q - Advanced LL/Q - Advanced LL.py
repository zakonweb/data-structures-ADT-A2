NULLPOINTER = -1
HeadOfQueue = EndOfQueue = FreeListPtr = CurrentNodePtr = 0
Queue = []

def InitialiseQueue():
    global HeadOfQueue, EndOfQueue, NULLPOINTER, FreeListPtr, Queue
    HeadOfQueue = EndOfQueue = NULLPOINTER
    FreeListPtr = 0
    for index in range(8):
        Queue.append(Node("", index + 1))
    Queue[7].Pointer = NULLPOINTER


def LeaveQueue():
    global HeadOfQueue, EndOfQueue, NULLPOINTER, FreeListPtr, Queue
    if HeadOfQueue == NULLPOINTER:
        print("Empty Queue")
        Value = ""
    else:
        Value = Queue[HeadOfQueue].Data
        ThisNodePtr = Queue[HeadOfQueue].Pointer
        if ThisNodePtr == NULLPOINTER:
            EndOfQueue = NULLPOINTER
        Queue[HeadOfQueue].Pointer = FreeListPtr
        FreeListPtr = HeadOfQueue
        HeadOfQueue = ThisNodePtr
    return Value


def JoinQueue(NewItem):
    global HeadOfQueue, EndOfQueue, NULLPOINTER, FreeListPtr, Queue
    if FreeListPtr != NULLPOINTER:
        NewNodePtr = FreeListPtr
        Queue[NewNodePtr].Data = NewItem
        FreeListPtr = Queue[FreeListPtr].Pointer
        Queue[NewNodePtr].Pointer = NULLPOINTER

        if EndOfQueue == NULLPOINTER:
            HeadOfQueue = NewNodePtr
        else:
            Queue[EndOfQueue].Pointer = NewNodePtr
        EndOfQueue = NewNodePtr
    else:
        print("no space for more data")


def OutputAllNodes():
    global HeadOfQueue, EndOfQueue, NULLPOINTER, FreeListPtr, Queue
    CurrentNodePtr = HeadOfQueue

    if HeadOfQueue == NULLPOINTER:
        print("No data in queue")

    while CurrentNodePtr != NULLPOINTER:
        print(CurrentNodePtr, Queue[CurrentNodePtr].Data)
        CurrentNodePtr = Queue[CurrentNodePtr].Pointer


def GetOption():
    print("1: Join queue\n2: Leave queue\n3: Output queue\n4: End program")
    print("Enter your choice: ")
    return int(input())


class Node:
    def __init__(self, Data, Pointer):
        self.Data = Data
        self.Pointer = Pointer


InitialiseQueue()
Choice = GetOption()
while Choice != 4:
    if Choice == 1:
        Data = input("Enter the value: ")
        JoinQueue(Data)
        OutputAllNodes()
    elif Choice == 2:
        Data = LeaveQueue()
        print("Data popped:", Data)
    elif Choice == 3:
        OutputAllNodes()
        print(HeadOfQueue, EndOfQueue)
        print(FreeListPtr)
        for i in range(8):
            print(i, Queue[i].Data)
            print(Queue[i].Pointer)
    Choice = GetOption()
