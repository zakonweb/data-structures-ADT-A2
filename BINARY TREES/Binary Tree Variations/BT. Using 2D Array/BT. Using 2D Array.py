# Constants
NULL_POINTER = -1
MAX_TREE_SIZE = 7

# Declare the Binary Tree
Root = None
BinaryTree = [[NULL_POINTER, NULL_POINTER, NULL_POINTER] for _ in range(MAX_TREE_SIZE)]

# Initialize the binary tree
def InitializeTree():
    global Root
    Root = NULL_POINTER
    for Index in range(MAX_TREE_SIZE):
        BinaryTree[Index][0] = NULL_POINTER
        BinaryTree[Index][1] = NULL_POINTER
        BinaryTree[Index][2] = NULL_POINTER

# Insert a node into the tree
def InsertNode(NewItem):
    global Root
    # Find an empty slot in the binary tree array for the new node
    NewNodePtr = None
    for Index in range(MAX_TREE_SIZE):
        if BinaryTree[Index][0] == NULL_POINTER:
            NewNodePtr = Index
            break

    if NewNodePtr is None:
        print("Binary Tree is full. Cannot insert new node.")
        return

    # Store data item and set null pointers for the new node
    BinaryTree[NewNodePtr][0] = NewItem
    BinaryTree[NewNodePtr][1] = NULL_POINTER
    BinaryTree[NewNodePtr][2] = NULL_POINTER

    # Check if empty tree
    if Root == None: # NULL_POINTER: # Insert new node at root
        Root = NewNodePtr
    else: # Find insertion point
        ThisNodePtr = Root # Start at the root of the tree
        PreviousNodePtr = NULL_POINTER
        while ThisNodePtr != NULL_POINTER: # While not a leaf node
            PreviousNodePtr = ThisNodePtr # Remember this node
            if NewItem < BinaryTree[ThisNodePtr][0]: # Follow left pointer
                ThisNodePtr = BinaryTree[ThisNodePtr][1]
            else: # Follow right pointer
                ThisNodePtr = BinaryTree[ThisNodePtr][2]

        if PreviousNodePtr is not None:
            if NewItem < BinaryTree[PreviousNodePtr][0]:
                BinaryTree[PreviousNodePtr][1] = NewNodePtr
            else:
                BinaryTree[PreviousNodePtr][2] = NewNodePtr

# Iteratively search for a node in the tree
def IterativeSearch(SearchItem):
    ThisNodePtr = Root # Start at the root of the tree
    while ThisNodePtr != NULL_POINTER and BinaryTree[ThisNodePtr][0] != SearchItem: # While a pointer to follow and search item not found
        if SearchItem < BinaryTree[ThisNodePtr][0]: # Follow left pointer
            ThisNodePtr = BinaryTree[ThisNodePtr][1]
        else: # Follow right pointer
            ThisNodePtr = BinaryTree[ThisNodePtr][2]
    return ThisNodePtr # Returns null pointer if search item not found

# Recursively search for a node in the tree
def RecursiveSearch(NodePtr, SearchItem):
    if NodePtr == NULL_POINTER or BinaryTree[NodePtr][0] == SearchItem:
        return NodePtr
    elif SearchItem < BinaryTree[NodePtr][0]:
        return RecursiveSearch(BinaryTree[NodePtr][1], SearchItem)
    else:
        return RecursiveSearch(BinaryTree[NodePtr][2], SearchItem)

# In-order traversal subroutine: Performs an in-order traversal of the binary tree.
# NodePtr: The node pointer to start the traversal from.
def InOrderTraversal(NodePtr):
    if NodePtr != NULL_POINTER:
        # Traverse the left subtree
        InOrderTraversal(BinaryTree[NodePtr][1])
        # Process the current node
        print(BinaryTree[NodePtr][0], end=" ")
        # Traverse the right subtree
        InOrderTraversal(BinaryTree[NodePtr][2])

# Pre-order traversal subroutine: Performs a pre-order traversal of the binary tree.
# NodePtr: The node pointer to start the traversal from.
def PreOrderTraversal(NodePtr):
    if NodePtr != NULL_POINTER:
        # Process the current node
        print(BinaryTree[NodePtr][0], end=" ")
        # Traverse the left subtree
        PreOrderTraversal(BinaryTree[NodePtr][1])
        # Traverse the right subtree
        PreOrderTraversal(BinaryTree[NodePtr][2])

# Post-order traversal subroutine: Performs a post-order traversal of the binary tree.
# NodePtr: The node pointer to start the traversal from.
def PostOrderTraversal(NodePtr):
    if NodePtr != NULL_POINTER:
        # Traverse the left subtree
        PostOrderTraversal(BinaryTree[NodePtr][1])
        # Traverse the right subtree
        PostOrderTraversal(BinaryTree[NodePtr][2])
        # Process the current node
        print(BinaryTree[NodePtr][0], end=" ")

# Subroutine to show the content of the binary tree array
def ShowBinaryTreeArray():
    print("Binary Tree Array Content:")
    for Index in range(MAX_TREE_SIZE):
        if BinaryTree[Index][0] != NULL_POINTER:
            print(f"Index:{Index} Data:{BinaryTree[Index][0]} Left Child:{BinaryTree[Index][1]} Right Child:{BinaryTree[Index][2]}")
        else:
            print(f"Index:{Index} Empty")

# function to visualise the binary tree with edges
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
        tree[level][pos] = BinaryTree[node][0]
        visualize_tree(BinaryTree[node][1], level+1, pos-2**(MAX_TREE_SIZE-level-2))
        visualize_tree(BinaryTree[node][2], level+1, pos+2**(MAX_TREE_SIZE-level-2))
    # call the function to visualize the tree
    visualize_tree(Root, 0, 2**(MAX_TREE_SIZE-1)-1)
    # print the tree
    print_tree(tree)

# Main program
# Variables
Choice = None
SearchItem = None
NewItem = None

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