```
// Constants
CONSTANT NULL_POINTER = -1
CONSTANT MAX_TREE_SIZE = 7

// TreeNode Record
TYPE TreeNode
    DECLARE Data : STRING
    DECLARE LeftChild : INTEGER
    DECLARE RightChild : INTEGER
ENDTYPE

// Declare the Binary Tree and Pointers
DECLARE Root : INTEGER
DECLARE FreePointer : INTEGER
DECLARE BinaryTree : ARRAY[0 : MAX_TREE_SIZE] OF TreeNode
```
```
// Main program
// Variables
ECLARE Choice : INTEGER
ECLARE SearchItem, NewItem : STRING

// Initialize the binary tree
CALL nitializeTree()

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
   OUTPUT "8. Exit"
   OUTPUT "Enter your choice (1-8):"
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
           ShowBinaryTreeArray
           OUTPUT ""

       8: // Exit
           OUTPUT "Exiting the program."

   ENDCASE
UNTIL Choice = 8
```
```
// Initialise the Binary Tree
PROCEDURE InitializeTree
    Root ← NULL_POINTER // set start pointer
    FreePointer ← 0 // set starting position of free list
    FOR Index ← 0 TO MAX_TREE_SIZE-1 // link all nodes to make free list
        BinaryTree[Index].LeftChild ← Index + 1
    NEXT Index
    BinaryTree[MAX_TREE_SIZE-1].LeftChild ← NULL_POINTER // last node of free list
ENDPROCEDURE
```
```
// Insert a node into the tree
PROCEDURE InsertNode(NewItem : STRING)
    IF FreePointer <> NULL_POINTER
    THEN // there is space in the array
        // take node from free list, store data item, set null pointers
        NewNodePtr ← FreePointer
        FreePointer ← BinaryTree[FreePointer].LeftChild
        BinaryTree[NewNodePtr].Data ← NewItem
        BinaryTree[NewNodePtr].LeftChild ← NULL_POINTER
        BinaryTree[NewNodePtr].RightChild ← NULL_POINTER
        
        // check if empty tree
        IF Root = NULL_POINTER
        THEN // insert new node at root
            Root ← NewNodePtr
        ELSE // find insertion point
            ThisNodePtr ← Root // start at the root of the tree
            WHILE ThisNodePtr <> NULL_POINTER DO // while not a leaf node
                PreviousNodePtr ← ThisNodePtr // remember this node
                IF BinaryTree[ThisNodePtr].Data > NewItem
                THEN // follow left pointer
                    TurnedLeft ← TRUE
                    ThisNodePtr ← BinaryTree[ThisNodePtr].LeftChild
                ELSE // follow right pointer
                    TurnedLeft ← FALSE
                    ThisNodePtr ← BinaryTree[ThisNodePtr].RightChild
                ENDIF
            ENDWHILE

            IF TurnedLeft = TRUE
            THEN
                BinaryTree[PreviousNodePtr].LeftChild ← NewNodePtr
            ELSE
                BinaryTree[PreviousNodePtr].RightChild ← NewNodePtr
            ENDIF
        ENDIF
        OUTPUT "Item inserted successfully."
    ELSE // the tree is full, no space for a new node
        OUTPUT "Error: Binary tree is full. Cannot insert a new item."
    ENDIF
ENDPROCEDURE
```
```
// Iteratively search for a node in the tree
FUNCTION IterativeSearch(SearchItem : STRING) RETURNS INTEGER // returns pointer to node
    THIS_NODE_PTR ← Root // start at the root of the tree
    WHILE THIS_NODE_PTR <> NULL_POINTER // while a pointer to follow
    AND BinaryTree[THIS_NODE_PTR].Data <> SearchItem DO // and search item not found
        IF BinaryTree[THIS_NODE_PTR].Data > SearchItem
        THEN // follow left pointer
            THIS_NODE_PTR ← BinaryTree[THIS_NODE_PTR].LeftChild
        ELSE // follow right pointer
            THIS_NODE_PTR ← BinaryTree[THIS_NODE_PTR].RightChild
        ENDIF
    ENDWHILE
    RETURN THIS_NODE_PTR // will return null pointer if search item not found
ENDFUNCTION
```
```
// Recursively search for a node in the tree
FUNCTION RecursiveSearch(NodePtr : INTEGER, SearchItem : STRING) RETURNS INTEGER
    IF NodePtr = NULL_POINTER OR BinaryTree[NodePtr].Data = SearchItem
    THEN
        RETURN NodePtr
    ELSEIF BinaryTree[NodePtr].Data > SearchItem
    THEN
        RETURN RecursiveSearch(BinaryTree[NodePtr].LeftChild, SearchItem)
    ELSE
        RETURN RecursiveSearch(BinaryTree[NodePtr].RightChild, SearchItem)
    ENDIF
ENDFUNCTION
```
```
// InOrderTraversal subroutine: Performs an in-order traversal of the binary tree.
// NodePtr: The node pointer to start the traversal from.
PROCEDURE InOrderTraversal(NodePtr : INTEGER)
    IF NodePtr <> NULL_POINTER THEN
        // Traverse the left subtree
        InOrderTraversal(BinaryTree[NodePtr].LeftChild)
        // Process the current node
        OUTPUT BinaryTree[NodePtr].Data
        // Traverse the right subtree
        InOrderTraversal(BinaryTree[NodePtr].RightChild)
    ENDIF
ENDPROCEDURE
```
```
// PreOrderTraversal subroutine: Performs a pre-order traversal of the binary tree.
// NodePtr: The node pointer to start the traversal from.
PROCEDURE PreOrderTraversal(NodePtr : INTEGER)
    IF NodePtr <> NULL_POINTER THEN
        // Process the current node
        OUTPUT BinaryTree[NodePtr].Data
        // Traverse the left subtree
        PreOrderTraversal(BinaryTree[NodePtr].LeftChild)
        // Traverse the right subtree
        PreOrderTraversal(BinaryTree[NodePtr].RightChild)
    ENDIF
ENDPROCEDURE
```
```
// PostOrderTraversal subroutine: Performs a post-order traversal of the binary tree.
// NodePtr: The node pointer to start the traversal from.
PROCEDURE PostOrderTraversal(NodePtr : INTEGER)
    IF NodePtr <> NULL_POINTER THEN
        // Traverse the left subtree
        PostOrderTraversal(BinaryTree[NodePtr].LeftChild)
        // Traverse the right subtree
        PostOrderTraversal(BinaryTree[NodePtr].RightChild)
        // Process the current node
        OUTPUT BinaryTree[NodePtr].Data
    ENDIF
ENDPROCEDURE
```
```
// Subroutine to show the content of the binary tree array
PROCEDURE ShowBinaryTreeArray()
    OUTPUT "Root:", Root
    OUTPUT "Free Pointer:", FreePointer
    OUTPUT "Binary Tree Array Content:"
    FOR Index ← 0 TO MAX_TREE_SIZE-1
        OUTPUT "Index:", Index, " Left Child:", BinaryTree[Index].LeftChild, " Data:", BinaryTree[Index].Data, " Right Child:", BinaryTree[Index].RightChild
    NEXT Index
ENDPROCEDURE
```