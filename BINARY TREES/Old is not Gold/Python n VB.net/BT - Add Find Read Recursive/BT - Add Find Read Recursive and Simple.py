NULLPOINTER = -1
UB = 9
LB = 0
RootPointer = FreePtr = 0
StackPtr = NULLPOINTER
Tree = Stack = []


def InitialiseTree():
    global NULLPOINTER, UB, LB, RootPointer, FreePtr, StackPtr, TreeNode, Tree
    RootPointer = NULLPOINTER
    FreePtr = 0
    for i in range(LB, UB + 1):
        Tree.append(TreeNode(NULLPOINTER, "", i + 1))
    Tree[UB].RightPointer = NULLPOINTER


def GetOption():
    print(
        'Binary Tree Main Menu\n1: Add Data Item\n2:Find Data Item\n3: Read/Traverse Binary Tree Inorder (left-root-right)\n4: Quit')
    Choice = int(input('Menu option...? '))
    return Choice


def FindNode(SearchItem):
    global NULLPOINTER, UB, LB, RootPointer, FreePtr, StackPtr, TreeNode, Tree

    CurrentPtr = RootPointer

    while CurrentPtr != NULLPOINTER and Tree[CurrentPtr].Data != SearchItem:
        if SearchItem < Tree[CurrentPtr].Data:
            CurrentPtr = Tree[CurrentPtr].LeftPointer
        else:
            CurrentPtr = Tree[CurrentPtr].RightPointer

    return CurrentPtr


def InsertNode(NewItem):
    global NULLPOINTER, UB, LB, RootPointer, FreePtr, StackPtr, TreeNode, Tree
    if FreePtr != NULLPOINTER:
        NewNodePtr = FreePtr
        Tree[NewNodePtr].Data = NewItem
        FreePtr = Tree[FreePtr].RightPointer
        Tree[NewNodePtr].RightPointer = NULLPOINTER

        if RootPointer == NULLPOINTER:
            RootPointer = NewNodePtr
        else:
            CurrentPtr = RootPointer
            while CurrentPtr != NULLPOINTER:
                PrevNodePtr = CurrentPtr

                if NewItem < Tree[CurrentPtr].Data:
                    TurnedLeft = True
                    CurrentPtr = Tree[CurrentPtr].LeftPointer
                else:
                    TurnedLeft = False
                    CurrentPtr = Tree[CurrentPtr].RightPointer

            if TurnedLeft:
                Tree[PrevNodePtr].LeftPointer = NewNodePtr
            else:
                Tree[PrevNodePtr].RightPointer = NewNodePtr
    else:
        print("Overflow occured. No space for more data...")


def InOrderTraverse(Root):
    global NULLPOINTER, UB, LB, RootPointer, FreePtr, StackPtr, TreeNode, Tree
    if Root != NULLPOINTER:
        InOrderTraverse(Tree[Root].LeftPointer)
        print(Tree[Root].Data)
        InOrderTraverse(Tree[Root].RightPointer)


def recursiveFind(currPtr, sVal):
    global NULLPOINTER, UB, LB, RootPointer, FreePtr, StackPtr, TreeNode, Tree
    if currPtr != NULLPOINTER:
        if Tree[currPtr].Data == sVal:
            return currPtr
        elif Tree[currPtr].Data > sVal:
            return recursiveFind(Tree[currPtr].LeftPointer, sVal)
        elif Tree[currPtr].Data < sVal:
            return recursiveFind(Tree[currPtr].RightPointer, sVal)
        else:
            return NULLPOINTER


def inorderIteration():
    global NULLPOINTER, UB, LB, RootPointer, FreePtr, StackPtr, TreeNode, Tree
    StackPtr = NULLPOINTER
    root = RootPointer

    while True:
        while root != NULLPOINTER:
            Push(root)
            root = Tree[root].LeftPointer

        if StackPtr == NULLPOINTER:
            break
        else:
            root = Pop()
            print(Stack[root].Data)
            root = Stack[root].RightPointer


def Pop():
    global NULLPOINTER, UB, LB, RootPointer, FreePtr, StackPtr, TreeNode, Tree
    currPtr = StackPtr
    StackPtr -= 1
    return currPtr


def Push(currPtr):
    global NULLPOINTER, UB, LB, RootPointer, FreePtr, StackPtr, TreeNode, Tree
    StackPtr += 1
    Stack[StackPtr] = Tree[currPtr]


class TreeNode:
    def __init__(self, LeftPointer, Data, RightPointer):
        self.LeftPointer = LeftPointer
        self.Data = Data
        self.RightPointer = RightPointer


InitialiseTree()
Choice = 0
while Choice != 4:
    Choice = GetOption()
    if Choice == 1:
        Data = input("Enter new data item... ")
        InsertNode(Data)
    elif Choice == 2:
        Data = input("Emter search value: ")
        CurrentPtr = recursiveFind(RootPointer, Data)
        if CurrentPtr == NULLPOINTER:
            print("Value not found")
        else:
            print("Value found at:", CurrentPtr)
    elif Choice == 3:
        print("Inorder Traversed Data\n----------------------")
        InOrderTraverse(RootPointer)

        print("\nRoot Pointer =", RootPointer, ", Free Pointer =", FreePtr, "\n")
        print("Index", "LP  ", "Data", " "*24, "RP")
        for i in range(LB,UB+1):
            print(i, " "*3, Tree[i].LeftPointer, " "*(3 - len(str(Tree[i].LeftPointer))), Tree[i].Data, " "*(28 - len(Tree[i].Data)), Tree[i].RightPointer)
