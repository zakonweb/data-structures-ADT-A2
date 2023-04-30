```
// Constants
CONSTANT NULL_POINTER = -1
CONSTANT MAX_TREE_SIZE = 7

// Declare the Binary Tree
DECLARE Root : INTEGER
DECLARE BinaryTree : ARRAY[1 : MAX_TREE_SIZE, 1 : 3] OF INTEGER

// Create a 2D array to store the tree and the edges
DECLARE Tree : ARRAY[1 : MAX_TREE_SIZE, 1 : (2^MAX_TREE_SIZE)] OF CHARACTER
```
```
// Main program
// Initialize the binary tree
CALL InitializeTree()

// Variables
DECLARE Choice : INTEGER
DECLARE SearchItem, NewItem : INTEGER

// Main loop
REPEAT
    // Display menu
    OUTPUT "Binary Tree Operations Menu:"
    OUTPUT "1. Insert a node"
    OUTPUT "2. Search for a node (Iteratively)"
    OUTPUT "3. Search for a node (Recursively)"
    OUTPUT "4. In-order traversal"
    OUTPUT "5. Pre-order traversal"
    OUTPUT "6. Post-order traversal"
    OUTPUT "7. Show Binary Tree Array Content"
    OUTPUT "8. Visualize Binary Tree with Edges"
    OUTPUT "9. Exit"
    OUTPUT "Enter your choice (1-9):"
    INPUT Choice

    // Perform the chosen operation
    CASE OF Choice
        1: // Insert a node
            OUTPUT "Enter the item to be inserted:"
            INPUT NewItem
            InsertNode(NewItem)
            OUTPUT "Item inserted successfully."

        2: // Search for a node (Iteratively)
            OUTPUT "Enter the item to search for:"
            INPUT SearchItem
            DECLARE NodePointer : INTEGER
            NodePointer ← IterativeSearch(SearchItem)
            IF NodePointer = NULL_POINTER THEN
                OUTPUT "Item not found."
            ELSE
                OUTPUT "Item found at node pointer:", NodePointer
            ENDIF

        3: // Search for a node (Recursively)
            OUTPUT "Enter the item to search for:"
            INPUT SearchItem
            DECLARE RecursiveNodePointer : INTEGER
            RecursiveNodePointer ← RecursiveSearch(Root, SearchItem)
            IF RecursiveNodePointer = NULL_POINTER THEN
                OUTPUT "Item not found."
            ELSE
                OUTPUT "Item found at node pointer:", RecursiveNodePointer
            ENDIF

        4: // In-order traversal
            OUTPUT "In-order traversal:"
            InOrderTraversal(Root)
            OUTPUT ""

        5: // Pre-order traversal
            OUTPUT "Pre-order traversal:"
            PreOrderTraversal(Root)
            OUTPUT ""

        6: // Post-order traversal
            OUTPUT "Post-order traversal:"
            PostOrderTraversal(Root)
            OUTPUT ""

        7: // Show Binary Tree Array Content
            ShowBinaryTreeArray()
            OUTPUT ""

        8: // Visualize Binary Tree with Edges
            CALL VisualizeBinaryTreeWithEdges()
            OUTPUT ""

        9: // Exit
            OUTPUT "Exiting the program."
    ENDCASE
UNTIL Choice = 9
```
```
// Initialize the Binary Tree
PROCEDURE InitializeTree
    Root ← NULL_POINTER // Set start pointer
    FOR Index ← 1 TO MAX_TREE_SIZE // Initialize all nodes as empty
        BinaryTree[Index, 1] ← NULL_POINTER
        BinaryTree[Index, 2] ← NULL_POINTER
        BinaryTree[Index, 3] ← NULL_POINTER
    NEXT Index
ENDPROCEDURE
```
```
// Insert a node into the tree
PROCEDURE InsertNode(NewItem : INTEGER)
    // Find an empty slot in the binary tree array for the new node
    DECLARE NewNodePtr, ThisNodePtr, PreviousNodePtr : INTEGER
    NewNodePtr ← NULL_POINTER
    FOR Index ← 1 TO MAX_TREE_SIZE
        IF BinaryTree[Index, 1] = NULL_POINTER THEN
            NewNodePtr ← Index
            EXIT FOR
        ENDIF
    NEXT Index

    IF NewNodePtr = NULL_POINTER THEN
        OUTPUT "Binary Tree is full. Cannot insert new node."
        EXIT PROCEDURE
    ENDIF

    // Store data item and set null pointers for the new node
    BinaryTree[NewNodePtr, 1] ← NewItem
    BinaryTree[NewNodePtr, 2] ← NULL_POINTER
    BinaryTree[NewNodePtr, 3] ← NULL_POINTER

    // Check if empty tree
    IF Root = NULL_POINTER THEN // Insert new node at root
        Root ← NewNodePtr
    ELSE // Find insertion point
        ThisNodePtr ← Root // Start at the root of the tree
        WHILE ThisNodePtr <> NULL_POINTER DO // While not a leaf node
            PreviousNodePtr ← ThisNodePtr // Remember this node
            IF NewItem < BinaryTree[ThisNodePtr, 1] THEN // Follow left pointer
                ThisNodePtr ← BinaryTree[ThisNodePtr, 2]
            ELSE // Follow right pointer
                ThisNodePtr ← BinaryTree[ThisNodePtr, 3]
            ENDIF
        ENDWHILE

        IF NewItem < BinaryTree[PreviousNodePtr, 1] THEN
            BinaryTree[PreviousNodePtr, 2] ← NewNodePtr
        ELSE
            BinaryTree[PreviousNodePtr, 3] ← NewNodePtr
        ENDIF
    ENDIF
ENDPROCEDURE
```
```
// Iteratively search for a node in the tree
FUNCTION IterativeSearch(SearchItem : INTEGER) RETURNS INTEGER // Returns pointer to node
    DECLARE ThisNodePtr : INTEGER
    ThisNodePtr ← Root // Start at the root of the tree
    WHILE ThisNodePtr <> NULL_POINTER AND BinaryTree[ThisNodePtr, 1] <> SearchItem DO // While a pointer to follow and search item not found
        IF SearchItem < BinaryTree[ThisNodePtr, 1] THEN // Follow left pointer
            ThisNodePtr ← BinaryTree[ThisNodePtr, 2]
        ELSE // Follow right pointer
            ThisNodePtr ← BinaryTree[ThisNodePtr, 3]
        ENDIF
    ENDWHILE
    RETURN ThisNodePtr // Returns null pointer if search item not found
ENDFUNCTION
```
```
// Recursively search for a node in the tree
FUNCTION RecursiveSearch(NodePtr : INTEGER, SearchItem : INTEGER) RETURNS INTEGER
    IF NodePtr = NULL_POINTER OR BinaryTree[NodePtr, 1] = SearchItem THEN
        RETURN NodePtr
    ELSEIF SearchItem < BinaryTree[NodePtr, 1] THEN
        RETURN RecursiveSearch(BinaryTree[NodePtr, 2], SearchItem)
    ELSE
        RETURN RecursiveSearch(BinaryTree[NodePtr, 3], SearchItem)
    ENDIF
ENDFUNCTION
```
```
// In-order traversal subroutine: Performs an in-order traversal of the binary tree.
// NodePtr: The node pointer to start the traversal from.
PROCEDURE InOrderTraversal(NodePtr : INTEGER)
    IF NodePtr <> NULL_POINTER THEN
        // Traverse the left subtree
        InOrderTraversal(BinaryTree[NodePtr, 2])
        // Process the current node
        OUTPUT BinaryTree[NodePtr, 1]
        // Traverse the right subtree
        InOrderTraversal(BinaryTree[NodePtr, 3])
    ENDIF
ENDPROCEDURE
```
```
// Pre-order traversal subroutine: Performs a pre-order traversal of the binary tree.
// NodePtr: The node pointer to start the traversal from.
PROCEDURE PreOrderTraversal(NodePtr : INTEGER)
    IF NodePtr <> NULL_POINTER THEN
        // Process the current node
        OUTPUT BinaryTree[NodePtr, 1]
        // Traverse the left subtree
        PreOrderTraversal(BinaryTree[NodePtr, 2])
        // Traverse the right subtree
        PreOrderTraversal(BinaryTree[NodePtr, 3])
    ENDIF
ENDPROCEDURE
```
```
// Post-order traversal subroutine: Performs a post-order traversal of the binary tree.
// NodePtr: The node pointer to start the traversal from.
PROCEDURE PostOrderTraversal(NodePtr : INTEGER)
    IF NodePtr <> NULL_POINTER THEN
        // Traverse the left subtree
        PostOrderTraversal(BinaryTree[NodePtr, 2])
        // Traverse the right subtree
        PostOrderTraversal(BinaryTree[NodePtr, 3])
        // Process the current node
        OUTPUT BinaryTree[NodePtr, 1]
    ENDIF
ENDPROCEDURE
```
```
// Subroutine to show the content of the binary tree array
PROCEDURE ShowBinaryTreeArray()
    OUTPUT "Binary Tree Array Content:"
    FOR Index ← 1 TO MAX_TREE_SIZE
        IF BinaryTree[Index, 1] <> NULL_POINTER THEN
            OUTPUT "Index:", Index, " Data:", BinaryTree[Index, 1], " Left Child:", BinaryTree[Index, 2], " Right Child:", BinaryTree[Index, 3]
        ELSE
            OUTPUT "Index:", Index, " Empty"
        ENDIF
    NEXT Index
ENDPROCEDURE
```
```
// Function to visualize the binary tree with edges
// '/' will be used to show the left child and '\' will be used to show the right child
// First create a 2D array to store the tree and the edges
// Then create a function to print the tree
PROCEDURE VisualizeBinaryTreeWithEdges()
    // Initialize the Tree array with spaces
    FOR RowIndex ← 1 TO MAX_TREE_SIZE
        FOR ColIndex ← 1 TO (2^MAX_TREE_SIZE)
            Tree[RowIndex, ColIndex] ← ' '
        NEXT ColIndex
    NEXT RowIndex

    // call the procedure to visualize the tree
    CALL VisualizeTree(Root, 0, 2^(MAX_TREE_SIZE-1)-1)
    // print the tree
    CALL PrintTree(tree)
END PROCEDURE
```
```
// Function to print the tree
PROCEDURE PrintTree()
    FOR RowIndex ← 1 TO MAX_TREE_SIZE
        DECLARE RowAsString : STRING
        FOR ColIndex ← 1 TO (2^MAX_TREE_SIZE)
            RowAsString ← RowAsString & Tree[RowIndex, ColIndex]
        NEXT ColIndex
        OUTPUT RowAsString
    NEXT RowIndex
ENDPROCEDURE
```
```
// Function to visualize the tree
PROCEDURE VisualizeTree(Node : INTEGER, Level : INTEGER, Position : INTEGER)
    IF Node = NULL_POINTER THEN
        EXIT PROCEDURE
    ENDIF
    Tree[Level, Position] ← BinaryTree[Node, 1]
    VisualizeTree(BinaryTree[Node, 2], Level + 1, Position - 2^(MAX_TREE_SIZE - Level - 2))
    VisualizeTree(BinaryTree[Node, 3], Level + 1, Position + 2^(MAX_TREE_SIZE - Level - 2))
ENDPROCEDURE
```
