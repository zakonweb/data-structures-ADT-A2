# Binary Tree Implementation

This code is for a Binary Tree (BT) implementation using a 1D array of a user-defined Node data type. A Binary Search Tree is a binary tree data structure where each node has at most two children, and for all nodes, the left child node's value is less than or equal to the parent node's value, and the right child node's value is greater than or equal to the parent node's value. This property ensures that a search operation in a BST has a logarithmic time complexity. 

## Explanation of the Code

### Constants
- `NULL_POINTER`: -1
- `MAX_TREE_SIZE`: 7

NULL_POINTER is used to indicate an empty node, while MAX_TREE_SIZE limits the size of the binary tree.

### Data Structures

The BinaryTree array stores nodes, where each node has an integer value (`Data`) and two pointers to its left and right children (`Left` and `Right`).

### Node data type

The Node data type is defined with three fields:
- `Data`: an integer
- `Left`: an integer pointer for the left child
- `Right`: an integer pointer for the right child

### InitializeTree procedure

This procedure initializes the binary tree by setting all nodes' Data, Left, and Right pointers to NULL_POINTER.

### Main Program Loop

The program displays a menu with options for different binary tree operations. The user selects an operation by inputting a choice, which then triggers the appropriate case statement.

### Procedures and Functions for Tree Operations

- `InsertNode`: Inserts a new node with a given integer value (`NewItem`) into the binary tree.
- `IterativeSearch`: Searches for a node with a given integer value (`SearchItem`) iteratively and returns the node's pointer if found.
- `RecursiveSearch`: Searches for a node with a given integer value (`SearchItem`) recursively and returns the node's pointer if found.
- `InOrderTraversal`, `PreOrderTraversal`, and `PostOrderTraversal`: These three procedures perform different tree traversal techniques (in-order, pre-order, and post-order) starting from the root of the tree and print the node values.
- `ShowBinaryTreeArray`: Displays the contents of the binary tree array, including the index, data, left child pointer, and right child pointer.
- `VisualizeBinaryTreeWithEdges`: Visualizes the binary tree structure using edges, making it easier to understand the tree's layout.

By using a 1D array to store the Node data type, this implementation of a Binary Search Tree provides a simple and efficient way to perform operations like insertion, searching, and traversal while maintaining the essential properties of a Binary Tree.
