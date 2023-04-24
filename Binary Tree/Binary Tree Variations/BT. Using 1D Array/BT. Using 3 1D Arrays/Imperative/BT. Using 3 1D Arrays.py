# Constants
NULL_POINTER = -1
MAX_TREE_SIZE = 7

# Declare the Binary Tree
Root = None
LeftChild = [NULL_POINTER] * MAX_TREE_SIZE
Data = [NULL_POINTER] * MAX_TREE_SIZE
RightChild = [NULL_POINTER] * MAX_TREE_SIZE

# Initialize the binary tree
def InitializeTree():
    global Root
    Root = NULL_POINTER
    for Index in range(MAX_TREE_SIZE):
        LeftChild[Index] = NULL_POINTER
        Data[Index] = NULL_POINTER
        RightChild[Index] = NULL_POINTER

# Insert a node into the tree
def InsertNode(NewItem):
    global Root
    # Find an empty slot in the binary tree array for the new node
    NewNodePtr = None
    for Index in range(MAX_TREE_SIZE):
        if Data[Index] == NULL_POINTER:
            NewNodePtr = Index
            break

    if NewNodePtr is None:
        print("Binary Tree is full. Cannot insert new node.")
        return

    # Store data item and set null pointers for the new node
    Data[NewNodePtr] = NewItem
    LeftChild[NewNodePtr] = NULL_POINTER
    RightChild[NewNodePtr] = NULL_POINTER

    # Check if empty tree
    if Root == NULL_POINTER: # Insert new node at root
        Root = NewNodePtr
    else: # Find insertion point
        ThisNodePtr = Root # Start at the root of the tree
        PreviousNodePtr = NULL_POINTER
        while ThisNodePtr != NULL_POINTER: # While not a leaf node
            PreviousNodePtr = ThisNodePtr # Remember this node
            if NewItem < Data[ThisNodePtr]: # Follow left pointer
                ThisNodePtr = LeftChild[ThisNodePtr]
            else: # Follow right pointer
                ThisNodePtr = RightChild[ThisNodePtr]

        if NewItem < Data[PreviousNodePtr]:
            LeftChild[PreviousNodePtr] = NewNodePtr
        else:
            RightChild[PreviousNodePtr] = NewNodePtr

# Iteratively search for a node in the tree
def IterativeSearch(SearchItem):
    ThisNodePtr = Root # Start at the root of the tree
    while ThisNodePtr != NULL_POINTER and Data[ThisNodePtr] != SearchItem: # While a pointer to follow and search item not found
        if SearchItem < Data[ThisNodePtr]: # Follow left pointer
            ThisNodePtr = LeftChild[ThisNodePtr]
        else: # Follow right pointer
            ThisNodePtr = RightChild[ThisNodePtr]
    return ThisNodePtr # Returns null pointer if search item not found

# Recursively search for a node in the tree
def RecursiveSearch(NodePtr, SearchItem):
    if NodePtr == NULL_POINTER or Data[NodePtr] == SearchItem:
        return NodePtr
    elif SearchItem < Data[NodePtr]:
        return RecursiveSearch(LeftChild[NodePtr], SearchItem)
    else:
        return RecursiveSearch(RightChild[NodePtr], SearchItem)

# In-order traversal subroutine: Performs an in-order traversal of the binary tree.
# NodePtr: The node pointer to start the traversal from.
def InOrderTraversal(NodePtr):
    if NodePtr != NULL_POINTER:
        # Traverse the left subtree
        InOrderTraversal(LeftChild[NodePtr])
        # Process the current node
        print(Data[NodePtr], end=" ")
        # Traverse the right subtree
        InOrderTraversal(RightChild[NodePtr])

# Pre-order traversal subroutine: Performs a pre-order traversal of the binary tree.
# NodePtr: The node pointer to start the traversal from.
def PreOrderTraversal(NodePtr):
    if NodePtr != NULL_POINTER:
        # Process the current node
        print(Data[NodePtr], end=" ")
        # Traverse the left subtree
        PreOrderTraversal(LeftChild[NodePtr])
        # Traverse the right subtree
        PreOrderTraversal(RightChild[NodePtr])

# Post-order traversal subroutine: Performs a post-order traversal of the binary tree.
# NodePtr: The node pointer to start the traversal from.
def PostOrderTraversal(NodePtr):
    if NodePtr != NULL_POINTER:
        # Traverse the left subtree
        PostOrderTraversal(LeftChild[NodePtr])
        # Traverse the right subtree
        PostOrderTraversal(RightChild[NodePtr])
        # Process the current node
        print(Data[NodePtr], end=" ")

# Subroutine to show the content of the binary tree array
def ShowBinaryTreeArray():
    print("Binary Tree Array Content:")
    for Index in range(MAX_TREE_SIZE):
        if Data[Index] != NULL_POINTER:
            print(f"Index:{Index} Data:{Data[Index]} Left Child:{LeftChild[Index]} Right Child:{RightChild[Index]}")
        else:
            print(f"Index:{Index} Empty")

# function to visualize the binary tree with edges
# / will be used to show left child and \ will be used to show right child
# first create a list of lists to store the tree and the edges
# then create a function to print the tree
def VisualizeBinaryTreeWithEdges():
    # create a list of lists to store the tree and the edges
    tree = [[' ' for x in range(2**MAX_TREE_SIZE)] for y in range(MAX_TREE_SIZE)]
    # create a function to print the tree
    def print_tree(tree):
        for row in tree:
            print(''.join([str(elem) for elem in row]))
    # function to visualize the tree
    def visualize_tree(node, level, pos):
        if node == NULL_POINTER:
            return
        tree[level][pos] = Data[node]
        visualize_tree(LeftChild[node], level+1, pos-2**(MAX_TREE_SIZE-level-2))
        visualize_tree(RightChild[node], level+1, pos+2**(MAX_TREE_SIZE-level-2))
        # draw edges
        if LeftChild[node] != NULL_POINTER:
            tree[level+1][pos-1] = '/'
        if RightChild[node] != NULL_POINTER:
            tree[level+1][pos+1] = '\\'
    # call the function to visualize the tree
    visualize_tree(Root, 0, 2**(MAX_TREE_SIZE-1)-1)
    # print the tree
    print_tree(tree)

# Main program
# Variables
Choice = None
SearchItem = None
NewItem = None

# Initialize the binary tree
InitializeTree()

# Main loop
while Choice != 9:
    # Display menu
    print("Binary Tree Operations Menu:")
    print("1. Insert a node")
    print("2. Search for a node (Iteratively)")
    print("3. Search for a node (Recursively)")
    print("4. In-order traversal")
    print("5. Pre-order traversal")
    print("6. Post-order traversal")
    print("7. Show Binary Tree Array Content")
    print("8. Visualize Binary Tree with Edges")
    print("9. Exit")
    Choice = int(input("Enter your choice (1-9): "))

    # Perform the chosen operation
    if Choice == 1: # Insert a node
        NewItem = int(input("Enter the item to be inserted: "))
        InsertNode(NewItem)
        print("Item inserted successfully.")
    elif Choice == 2: # Search for a node (Iteratively)
        SearchItem = int(input("Enter the item to search for: "))
        NodePointer = IterativeSearch(SearchItem)
        if NodePointer == NULL_POINTER:
            print("Item not found.")
        else:
            print(f"Item found at node pointer: {NodePointer}")
    elif Choice == 3: # Search for a node (Recursively)
        SearchItem = int(input("Enter the item to search for: "))
        RecursiveNodePointer = RecursiveSearch(Root, SearchItem)
        if RecursiveNodePointer == NULL_POINTER:
            print("Item not found.")
        else:
            print(f"Item found at node pointer: {RecursiveNodePointer}")
    elif Choice == 4: # In-order traversal
        print("In-order traversal:", end=" ")
        InOrderTraversal(Root)
        print()
    elif Choice == 5: # Pre-order traversal
        print("Pre-order traversal:", end=" ")
        PreOrderTraversal(Root)
        print()
    elif Choice == 6: # Post-order traversal
        print("Post-order traversal:", end=" ")
        PostOrderTraversal(Root)
        print()
    elif Choice == 7: # Show Binary Tree Array Content
        ShowBinaryTreeArray()
    elif Choice == 8:  # Visualize Binary Tree with Edges
        print("Binary Tree visualization with edges:")
        VisualizeBinaryTreeWithEdges()
    elif Choice == 9: # Exit
        print("Exiting the program.")
    else:
        print("Invalid choice. Please enter a number from 1 to 9.")
