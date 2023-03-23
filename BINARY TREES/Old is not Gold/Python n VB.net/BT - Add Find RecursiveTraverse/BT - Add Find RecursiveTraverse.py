NULLPOINTER = -1
RootPointer = FreePtr = 0
Tree = []


def InitialiseTree():
    global TreeNode, RootPointer, FreePtr, NULLPOINTER, Tree
    RootPointer = NULLPOINTER
    FreePtr = 0
    for index in range(8):
        Tree.append(TreeNode("", index + 1, NULLPOINTER))
    Tree[7].LeftPointer = NULLPOINTER


def FindNode(SearchItem):
    global TreeNode, RootPointer, FreePtr, NULLPOINTER, Tree
    ThisNodePtr = RootPointer
    try:
        while ThisNodePtr != NULLPOINTER and Tree[ThisNodePtr].Data != SearchItem:
            if Tree[ThisNodePtr].Data > SearchItem:
                ThisNodePtr = Tree[ThisNodePtr].LeftPointer
            else:
                ThisNodePtr = Tree[ThisNodePtr].RightPointer
    except:
        None
    return ThisNodePtr


def InsertNode(NewItem):
    global TreeNode, RootPointer, FreePtr, NULLPOINTER, Tree
    PreviousNodePtr = ThisNodePtr1 = NewNodePtr = 0
    TurnedLeft = False
    if FreePtr != NULLPOINTER:
        NewNodePtr = FreePtr
        Tree[NewNodePtr].Data = NewItem
        FreePtr = Tree[FreePtr].LeftPointer
        Tree[NewNodePtr].LeftPointer = NULLPOINTER

        if RootPointer == NULLPOINTER:
            RootPointer = NewNodePtr
        else:
            ThisNodePtr1 = RootPointer

            while ThisNodePtr1 != NULLPOINTER:
                PreviousNodePtr = ThisNodePtr1

                if Tree[ThisNodePtr1].Data > NewItem:
                    TurnedLeft = True
                else:
                    TurnedLeft = False
                    ThisNodePtr1 = Tree[ThisNodePtr1].RightPointer

            if TurnedLeft:
                Tree[PreviousNodePtr].LeftPointer = NewNodePtr
            else:
                Tree[PreviousNodePtr].RightPointer = NewNodePtr
    else:
        print("Overflow - No space for more data")


def TraverseTree(RootPointer):
    global TreeNode, FreePtr, NULLPOINTER, Tree
    if RootPointer != NULLPOINTER:
        TraverseTree(Tree[RootPointer].LeftPointer)
        print(Tree[RootPointer].Data)
        TraverseTree(Tree[RootPointer].RightPointer)


def GetOption():
    print("1: Add data\n2: Find data\n3: Traverse tree\n4: End program")
    Choice = int(input("Enter your choice: "))
    return Choice


class TreeNode:
    def __init__(self, Data, LeftPointer, RightPointer):
        self.Data = Data
        self.LeftPointer = LeftPointer
        self.RightPointer = RightPointer


InitialiseTree()
Choice = GetOption()

while Choice != 4:
    if Choice == 1:
        Data = input("Enter the value: ")
        InsertNode(Data)
        TraverseTree(RootPointer)
    elif Choice == 2:
        Data = input("Enter search value: ")
        ThisNodePtr = FindNode(Data)
        if ThisNodePtr == NULLPOINTER:
            print("Value not found")
        else:
            print("value found at:", ThisNodePtr)
        print(RootPointer, FreePtr)
        for i in range(8):
            print(i, Tree[i].LeftPointer, Tree[i].Data, Tree[i].RightPointer)
    elif Choice == 3:
        TraverseTree(RootPointer)
    Choice = GetOption()