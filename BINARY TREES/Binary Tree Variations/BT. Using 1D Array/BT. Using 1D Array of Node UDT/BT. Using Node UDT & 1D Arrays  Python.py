# Constants
NULL_POINTER = -1
MAX_TREE_SIZE = 7

# Define the Node class
class Node:
    def __init__(self, data=NULL_POINTER, left=NULL_POINTER, right=NULL_POINTER):
        self.data = data
        self.left = left
        self.right = right

# Initialize the Binary Tree with empty Nodes
BinaryTree = [Node() for _ in range(MAX_TREE_SIZE)]

# Function to initialize the Binary Tree with NULL_POINTER values
def initialize_tree():
    for index in range(MAX_TREE_SIZE):
        BinaryTree[index].data = NULL_POINTER
        BinaryTree[index].left = NULL_POINTER
        BinaryTree[index].right = NULL_POINTER

def insert_node(new_item: int):
    global BinaryTree

    # Find an empty slot in the binary tree array for the new node
    new_node_ptr = NULL_POINTER
    for index in range(MAX_TREE_SIZE):
        if BinaryTree[index].data == NULL_POINTER:
            new_node_ptr = index
            break

    if new_node_ptr == NULL_POINTER:
        print("Binary Tree is full. Cannot insert new node.")
        return

    # Check if empty tree
    if BinaryTree[0].data == NULL_POINTER:  # Insert new node at root
        BinaryTree[0] = Node(new_item, NULL_POINTER, NULL_POINTER)
    else:  # Find insertion point
        # Store data item and set null pointers for the new node
        BinaryTree[new_node_ptr].data = new_item
        BinaryTree[new_node_ptr].left = NULL_POINTER
        BinaryTree[new_node_ptr].right = NULL_POINTER

        this_node_ptr = 0
        previous_node_ptr = NULL_POINTER

        while this_node_ptr != NULL_POINTER:
            previous_node_ptr = this_node_ptr
            if new_item < BinaryTree[this_node_ptr].data:
                if BinaryTree[this_node_ptr].left == NULL_POINTER:
                    break
                this_node_ptr = BinaryTree[this_node_ptr].left
            else:
                if BinaryTree[this_node_ptr].right == NULL_POINTER:
                    break
                this_node_ptr = BinaryTree[this_node_ptr].right

        if previous_node_ptr == NULL_POINTER and new_item > BinaryTree[0].data:
            # New item is greater than the root value
            BinaryTree[0].right = new_node_ptr
        elif previous_node_ptr == NULL_POINTER and new_item < BinaryTree[0].data:
            # New item is smaller than the root value
            BinaryTree[0].left = new_node_ptr
        elif new_item < BinaryTree[previous_node_ptr].data:
            BinaryTree[previous_node_ptr].left = new_node_ptr
        else:
            BinaryTree[previous_node_ptr].right = new_node_ptr


# Iteratively search for a node in the tree
def iterative_search(search_item):
    index = 0
    this_node_ptr = BinaryTree[0]
    while this_node_ptr.data != NULL_POINTER and this_node_ptr.data != search_item:
        if search_item < this_node_ptr.data:
            index = this_node_ptr.left
            this_node_ptr = BinaryTree[index]
        else:
            index = this_node_ptr.right
            this_node_ptr = BinaryTree[index]
    return NULL_POINTER if this_node_ptr.data != search_item else index

# Recursively search for a node in the tree
def recursive_search(node_ptr, search_item):
    if node_ptr == NULL_POINTER or BinaryTree[node_ptr].data == search_item:
        return node_ptr
    elif search_item < BinaryTree[node_ptr].data:
        return recursive_search(BinaryTree[node_ptr].left, search_item)
    else:
        return recursive_search(BinaryTree[node_ptr].right, search_item)

# In-order traversal subroutine
def in_order_traversal(node_ptr):
    if node_ptr.data != NULL_POINTER:
        in_order_traversal(BinaryTree[node_ptr.left])
        print(node_ptr.data, end=" ")
        in_order_traversal(BinaryTree[node_ptr.right])

# Pre-order traversal subroutine
def pre_order_traversal(node_ptr):
    if node_ptr.data != NULL_POINTER:
        print(node_ptr.data, end=" ")
        pre_order_traversal(BinaryTree[node_ptr.left])
        pre_order_traversal(BinaryTree[node_ptr.right])

# Post-order traversal subroutine
def post_order_traversal(node_ptr):
    if node_ptr.data != NULL_POINTER:
        post_order_traversal(BinaryTree[node_ptr.left])
        post_order_traversal(BinaryTree[node_ptr.right])
        print(node_ptr.data, end=" ")

import math
# Show Binary Tree Array Content subroutine
def show_binary_tree_array():
    print("Binary Tree Array Content:")
    print("Index | Data | Left | Right")
    for index in range(MAX_TREE_SIZE):
        node = BinaryTree[index]
        print(f"{index} | {node.data} | {node.left} | {node.right}")

"""# Function to visualize the binary tree
def visualize_binary_tree(node, level=0, position=0, tree=None):
    if tree is None:
        tree = [' '] * MAX_TREE_SIZE

    if node.data == NULL_POINTER:
        return
    
    MAX_TREE_DEPTH = int(math.log2(MAX_TREE_SIZE)) + 1
    tree[position] = str(node.data)
    if node.left != NULL_POINTER:
        visualize_binary_tree(BinaryTree[node.left], level + 1, position - 2 ** (MAX_TREE_DEPTH - level - 2), tree)
    if node.right != NULL_POINTER:
        visualize_binary_tree(BinaryTree[node.right], level + 1, position + 2 ** (MAX_TREE_DEPTH - level - 2), tree)

    if level == 0:  # Only print the tree after the root node is processed
        print_tree(tree)
"""
def visualize_binary_tree():
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
        tree[level][pos] = BinaryTree[node].data
        visualize_tree(BinaryTree[node].left, level+1, pos-2**(MAX_TREE_SIZE-level-2))
        visualize_tree(BinaryTree[node].right, level+1, pos+2**(MAX_TREE_SIZE-level-2))
        # draw edges
        if BinaryTree[node].left != NULL_POINTER:
            tree[level+1][pos-1] = '/'
        if BinaryTree[node].right != NULL_POINTER:
            tree[level+1][pos+1] = '\\'
    # call the function to visualize the tree
    visualize_tree(0, 0, 2**(MAX_TREE_SIZE-1)-1)
    # print the tree
    print_tree(tree)

def print_tree(tree):
    # Calculate the maximum level of the tree. For explanation, see comments after the function code.
    max_level = int(math.log2(len(tree))) + 1
    current_level = 0
    start_index = 0
    end_index = 0

    for index in range(len(tree)):
        if index == start_index:  # Start a new level
            print()  # Start a new line
            # Calculate the number of spaces before the first node in each level
            spaces_before = 2 ** (max_level - current_level - 1) - 1
            print(" " * spaces_before, end="")
            current_level += 1

        print(tree[index], end="")

        # Calculate the number of spaces between nodes in the current level
        spaces_between = 2 ** (max_level - current_level) - 1
        print(" " * spaces_between, end="")

        if index == end_index:  # End of current level
            start_index = end_index + 1
            end_index = end_index + 2 ** current_level

    print()  # Start a new line
    """
    The purpose of the max_level calculation is to find the maximum depth of the binary tree. 
    The calculation is based on the length (number of nodes) in the tree array.
    
    math.log2(len(tree)) computes the base-2 logarithm of the length of the tree array. 
    For a complete binary tree, the base-2 logarithm of the total number of nodes gives the 
    depth of the tree. However, the tree may not be complete, so the result of the logarithm 
    is rounded down to the nearest integer using int() to find the largest depth that is 
    guaranteed to have nodes.
    
    Finally, adding 1 to the result ensures that we include the root level in the maximum depth. 
    This value is used later in the print_tree function to calculate the appropriate number 
    of spaces before the first node of each level and between nodes in the current level, 
    ensuring a visually organized structure when printing the tree.
    """

# Main program
# Initialize the binary tree
initialize_tree()

while True:
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
    print("Enter your choice (1-9):", end=" ")

    choice = int(input())

    if choice == 1:  # Insert a node
        new_item = int(input("Enter the item to be inserted: "))
        insert_node(new_item)
        print("Item inserted successfully.")

    elif choice == 2:  # Search for a node (Iteratively)
        search_item = int(input("Enter the item to search for: "))
        node_pointer = iterative_search(search_item)
        if node_pointer == NULL_POINTER:
            print("Item not found.")
        else:
            print(f"Item found at node pointer: {node_pointer}")

    elif choice == 3:  # Search for a node (Recursively)
        search_item = int(input("Enter the item to search for: "))
        recursive_node_pointer = recursive_search(0, search_item)
        if recursive_node_pointer == NULL_POINTER:
            print("Item not found.")
        else:
            print(f"Item found at node pointer: {recursive_node_pointer}")

    elif choice == 4:  # In-order traversal
        print("In-order traversal:")
        in_order_traversal(BinaryTree[0])
        print()

    elif choice == 5:  # Pre-order traversal
        print("Pre-order traversal:")
        pre_order_traversal(BinaryTree[0])
        print()

    elif choice == 6:  # Post-order traversal
        print("Post-order traversal:")
        post_order_traversal(BinaryTree[0])
        print()

    elif choice == 7:  # Show Binary Tree Array Content
        show_binary_tree_array()
        print()

    elif choice == 8:  # Visualize Binary Tree with Edges
        visualize_binary_tree()
        print()

    elif choice == 9:  # Exit
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 9.")
