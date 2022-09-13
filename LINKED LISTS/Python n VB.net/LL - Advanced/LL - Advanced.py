# Declare record type to store data and pointer
class ListNode:
    def __init__(self):
        self.Data = ""
        self.Pointer = 0

# NullPointer should be set to -1
# if using array lb with index 0
NULLPOINTER = -1
StartPointer = 0
FreeListPtr = 0
CurrentNodePtr = 0
List = [ListNode() for i in range(9)]

def InitialiseList():
    global StartPointer, FreeListPtr, NULLPOINTER
    StartPointer = NULLPOINTER  # set start pointer
    FreeListPtr = 0  # set starting position of free list
    for Index in range(9):  # link all nodes to make free list
        List[Index].Pointer = Index + 1
    List[8].Pointer = NULLPOINTER

def InsertNode(NewItem):
    global StartPointer, FreeListPtr, NULLPOINTER
    if FreeListPtr != NULLPOINTER: # EXCEPTION
        # there is space in the array/list
        # take node from free list and store data item
        NewNodePtr = FreeListPtr
        List[NewNodePtr].Data = NewItem
        FreeListPtr = List[FreeListPtr].Pointer
        # find insertion point
        PreviousNodePtr = NULLPOINTER
        ThisNodePtr = StartPointer  # start at beginning of list
        try:
            while ThisNodePtr != NULLPOINTER and List[ThisNodePtr].Data < NewItem:
                # while not end of list
                PreviousNodePtr = ThisNodePtr  # remember this node
                # follow the pointer to the next node
                ThisNodePtr = List[ThisNodePtr].Pointer
        except:
            pass
        if PreviousNodePtr == NULLPOINTER:  # insert  new node at start of list
            List[NewNodePtr].Pointer = StartPointer
            StartPointer = NewNodePtr
        else:  # insert new node betweem previous node and this node
            List[PreviousNodePtr].Pointer = NewNodePtr
            List[NewNodePtr].Pointer = ThisNodePtr #Correction 1... List[PreviousNodePtr].Pointer
    else:
        print("Overflow. There is no space in memory for more data")

def OutputAllNodes():
    global StartPointer, NULLPOINTER
    CurrentNodePtr = StartPointer  # start at beginning of list
    if StartPointer == NULLPOINTER:
        print("No data in list.")
    while CurrentNodePtr != NULLPOINTER:  # while not end of list
        print(CurrentNodePtr, List[CurrentNodePtr].Data)
        # follow the pointer to the next node
        CurrentNodePtr = List[CurrentNodePtr].Pointer

def FindNode(DataItem):  # returns pointer to node
    global StartPointer, NULLPOINTER
    CurrentNodePtr = StartPointer  # start at beginning of list
    try:
        while CurrentNodePtr != NULLPOINTER and List[CurrentNodePtr].Data != DataItem:
            # not end of list, item not found
            # follow the pointer to the next node
            CurrentNodePtr = List[CurrentNodePtr].Pointer
    except:
        print("data not found")
    return CurrentNodePtr  # returns NULLPOINTER if item not found

def DeleteNode(DataItem):
    global StartPointer, FreeListPtr, NULLPOINTER
    if StartPointer == NULLPOINTER:
        print("Underflow occured. List is empty")
    ThisNodePtr = StartPointer
    try:
        # start at beginning of list
        while ThisNodePtr != NULLPOINTER and List[ThisNodePtr].Data != DataItem:
            # while not end of list and item not found
            PreviousNodePtr = ThisNodePtr  # remember this node
            # follow the pointer to the next node
            ThisNodePtr = List[ThisNodePtr].Pointer
    except:
        print("data does not exist in list")
    if ThisNodePtr != NULLPOINTER:  # node exists in list
        if ThisNodePtr == StartPointer:  # first node to be deleted
            StartPointer = List[StartPointer].Pointer
        else:
            List[PreviousNodePtr].Pointer = List[ThisNodePtr].Pointer
        List[ThisNodePtr].Pointer = FreeListPtr
        FreeListPtr = ThisNodePtr

def GetOption():
    print("Linked List Operations:")
    print("1: Insert a node")
    print("2: Delete a node")
    print("3: Find a node")
    print("4: Output list")
    print("5: End program")
    Choice = int(input("Enter your choice: "))
    return Choice

# main program
InitialiseList()
Choice = GetOption()
while Choice != 5:
    if Choice == 1:
        Data = input("Enter the value to insert in LL node: ")
        InsertNode(Data)
        #OutputAllNodes()
    elif Choice == 2:
        Data = input("Enter the value to delete from LL node: ")
        DeleteNode(Data)
        #OutputAllNodes()
    elif Choice == 3:
        Data = input("Enter the node value to look for in LL: ")
        CurrentNodePtr = FindNode(Data)
        if CurrentNodePtr == NULLPOINTER:
            print(Data, "couldn't be found.")
        else:
            print(Data, "found at: ", CurrentNodePtr)
    elif Choice == 4:
        print("Printing list in order.")
        OutputAllNodes()
        print("Printing array depiction")
        print("StartPointer= ", StartPointer, "FreeListPtr= ", FreeListPtr)
        for i in range(9):
            print(i, List[i].Data, List[i].Pointer)
    Choice = GetOption()