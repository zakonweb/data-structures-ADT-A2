```
// Constants
CONSTANT NULL_POINTER = -1
CONSTANT MAX_TREE_SIZE = 7

// Declare the Binary Tree
DECLARE BinaryTree : ARRAY[1 : MAX_TREE_SIZE] OF Node

// Define the Node data type
DEFINE TYPE Node
    Data : INTEGER
    Left : INTEGER
    Right : INTEGER
ENDTYPE

// Initialize the binary tree
CALL InitializeTree()
```
```
// Main program
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
            RecursiveNodePointer ← RecursiveSearch(BinaryTree[1], SearchItem)
            IF RecursiveNodePointer = NULL_POINTER THEN
                OUTPUT "Item not found."
            ELSE
                OUTPUT "Item found at node pointer:", RecursiveNodePointer
            ENDIF

        4: // In-order traversal
            OUTPUT "In-order traversal:"
            InOrderTraversal(BinaryTree[1])
            OUTPUT ""

        5: // Pre-order traversal
            OUTPUT "Pre-order traversal:"
            PreOrderTraversal(BinaryTree[1])
            OUTPUT ""

        6: // Post-order traversal
            OUTPUT "Post-order traversal:"
            PostOrderTraversal(BinaryTree[1])
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
    FOR Index ← 1 TO MAX_TREE_SIZE // Initialize all nodes as empty
        BinaryTree[Index].Data ← NULL_POINTER
        BinaryTree[Index].Left ← NULL_POINTER
        BinaryTree[Index].Right ← NULL_POINTER
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
        IF BinaryTree[Index].Data = NULL_POINTER THEN
            NewNodePtr ← Index
            EXIT FOR
        ENDIF
    NEXT Index

    IF NewNodePtr = NULL_POINTER THEN
        OUTPUT "Binary Tree is full. Cannot insert new node."
        EXIT PROCEDURE
    ENDIF

    // Check if empty tree
    IF BinaryTree[1].Data = NULL_POINTER THEN // Insert new node at root
        BinaryTree[1].Data ← NewItem
        BinaryTree[1].Left ← NULL_POINTER
        BinaryTree[1].Right ← NULL_POINTER    
    ELSE // Find insertion point
        // Store data item and set null pointers for the new node
        BinaryTree[NewNodePtr].Data ← NewItem
        BinaryTree[NewNodePtr].Left ← NULL_POINTER
        BinaryTree[NewNodePtr].Right ← NULL_POINTER

        ThisNodePtr ← 1 // Start at the root of the tree
        WHILE ThisNodePtr <> NULL_POINTER DO // While not a leaf node
            PreviousNodePtr ← ThisNodePtr // Remember this node
            IF NewItem < BinaryTree[ThisNodePtr].Data THEN // Follow left pointer
                ThisNodePtr ← BinaryTree[ThisNodePtr].Left
            ELSE // Follow right pointer
                ThisNodePtr ← BinaryTree[ThisNodePtr].Right
            ENDIF
        ENDWHILE

        IF NewItem < BinaryTree[PreviousNodePtr].Data THEN
            BinaryTree[PreviousNodePtr].Left ← NewNodePtr
        ELSE
            BinaryTree[PreviousNodePtr].Right ← NewNodePtr
        ENDIF
    ENDIF
ENDPROCEDURE
```
```
// Iteratively search for a node in the tree
FUNCTION IterativeSearch(SearchItem : INTEGER) RETURNS INTEGER // Returns pointer to node
    DECLARE ThisNodePtr : INTEGER
    ThisNodePtr ← BinaryTree[1]
    WHILE ThisNodePtr <> NULL_POINTER AND BinaryTree[ThisNodePtr].Data <> SearchItem DO
        IF SearchItem < BinaryTree[ThisNodePtr].Data THEN
            ThisNodePtr ← BinaryTree[ThisNodePtr].Left
        ELSE
            ThisNodePtr ← BinaryTree[ThisNodePtr].Right
        ENDIF
    ENDWHILE
    RETURN ThisNodePtr
ENDFUNCTION
```
```
// Recursively search for a node in the tree
FUNCTION RecursiveSearch(NodePtr : INTEGER, SearchItem : INTEGER) RETURNS INTEGER
    IF NodePtr = NULL_POINTER OR BinaryTree[NodePtr].Data = SearchItem THEN
        RETURN NodePtr
    ELSEIF SearchItem < BinaryTree[NodePtr].Data THEN
        RETURN RecursiveSearch(BinaryTree[NodePtr].Left, SearchItem)
    ELSE
        RETURN RecursiveSearch(BinaryTree[NodePtr].Right, SearchItem)
    ENDIF
ENDFUNCTION
```
```
// In-order traversal subroutine: Performs an in-order traversal of the binary tree.
// NodePtr: The node pointer to start the traversal from.
PROCEDURE InOrderTraversal(NodePtr : INTEGER)
    IF NodePtr <> NULL_POINTER THEN
        InOrderTraversal(BinaryTree[NodePtr].Left)
        OUTPUT BinaryTree[NodePtr].Data
        InOrderTraversal(BinaryTree[NodePtr].Right)
    ENDIF
ENDPROCEDURE
```
```
// Pre-order traversal subroutine: Performs a pre-order traversal of the binary tree.
// NodePtr: The node pointer to start the traversal from.
PROCEDURE PreOrderTraversal(NodePtr : INTEGER)
    IF NodePtr <> NULL_POINTER THEN
        OUTPUT BinaryTree[NodePtr].Data
        PreOrderTraversal(BinaryTree[NodePtr].Left)
        PreOrderTraversal(BinaryTree[NodePtr].Right)
    ENDIF
ENDPROCEDURE
```
```
// Post-order traversal subroutine: Performs a post-order traversal of the binary tree.
// NodePtr: The node pointer to start the traversal from.
PROCEDURE PostOrderTraversal(NodePtr : INTEGER)
    IF NodePtr <> NULL_POINTER THEN
        PostOrderTraversal(BinaryTree[NodePtr].Left)
        PostOrderTraversal(BinaryTree[NodePtr].Right)
        OUTPUT BinaryTree[NodePtr].Data
    ENDIF
ENDPROCEDURE
```
```
// Show Binary Tree Array Content subroutine: Displays the contents of the binary tree array.
PROCEDURE ShowBinaryTreeArray
    OUTPUT "Binary Tree Array Content:"
    OUTPUT "Index | Data | Left | Right"
    FOR Index ← 1 TO MAX_TREE_SIZE
        OUTPUT Index, " | ", BinaryTree[Index].Data, " | ", BinaryTree[Index].Left, " | ", BinaryTree[Index].Right
    NEXT Index
END PROCEDURE
```
```
// Visualize Binary Tree with Edges subroutine: Displays the binary tree with edges.
PROCEDURE VisualizeBinaryTreeWithEdges()
    // Initialize the Tree array with spaces
    FOR Index ← 1 TO MAX_TREE_SIZE
        Tree[Index] ← ' '
    NEXT Index

    // call the procedure to visualize the tree
    CALL VisualizeTree(Root, 0, 2^(MAX_TREE_SIZE-1)-1)
    // print the tree
    CALL PrintTree()
ENDPROCEDURE
```
```
// Function to print the tree
PROCEDURE PrintTree()
    DECLARE CurrentLevel, StartIndex, EndIndex, Index : INTEGER
    CurrentLevel ← 0
    StartIndex ← 1
    EndIndex ← 1
    FOR Index ← 1 TO MAX_TREE_SIZE
        IF Index = StartIndex THEN // Start a new level
            OUTPUT "" // Start a new line
            FOR SpaceIndex ← 1 TO 2^(MAX_TREE_SIZE - CurrentLevel - 1) - 1
                OUTPUT " "
            NEXT SpaceIndex
            CurrentLevel ← CurrentLevel + 1
        ENDIF
        OUTPUT Tree[Index]
        FOR SpaceIndex ← 1 TO 2^(MAX_TREE_SIZE - CurrentLevel) - 1
            OUTPUT " "
        NEXT SpaceIndex
        IF Index = EndIndex THEN // End of current level
            StartIndex ← EndIndex + 1
            EndIndex ← EndIndex + 2^CurrentLevel
        ENDIF
    NEXT Index
    OUTPUT "" // Start a new line
ENDPROCEDURE
```
```
// Function to visualize the tree
PROCEDURE VisualizeTree(Node : INTEGER, Level : INTEGER, Position : INTEGER)
    IF Node = NULL_POINTER THEN
        EXIT PROCEDURE
    ENDIF
    Tree[Position] ← Str(Node)
    VisualizeTree(BinaryTree[Node].Left, Level + 1, Position - 2^(MAX_TREE_SIZE - Level - 2))
    VisualizeTree(BinaryTree[Node].Right, Level + 1, Position + 2^(MAX_TREE_SIZE - Level - 2))
ENDPROCEDURE
```