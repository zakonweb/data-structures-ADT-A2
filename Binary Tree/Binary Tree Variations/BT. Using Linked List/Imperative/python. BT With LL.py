# Constants
NULL_POINTER = -1
MAX_TREE_SIZE = 7

# TreeNode Class
class TreeNode:
    def __init__(self, data='', left_child=NULL_POINTER, right_child=NULL_POINTER):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child

# Declare the Binary Tree and Pointers
root = NULL_POINTER
free_pointer = NULL_POINTER
binary_tree = [TreeNode() for _ in range(MAX_TREE_SIZE)]

# Initialize the binary tree
def initialize_tree():
    global root, free_pointer, binary_tree
    root = NULL_POINTER
    free_pointer = 0
    for index in range(MAX_TREE_SIZE - 1):
        binary_tree[index].left_child = index + 1
    binary_tree[MAX_TREE_SIZE - 1].left_child = NULL_POINTER

# Insert a node into the tree
def insert_node(new_item):
    global root, free_pointer, binary_tree

    if free_pointer != NULL_POINTER:
        # There is space in the array
        # Take a node from the free list, store data item, and set null pointers
        new_node_ptr = free_pointer
        free_pointer = binary_tree[free_pointer].left_child
        binary_tree[new_node_ptr].data = new_item
        binary_tree[new_node_ptr].left_child = NULL_POINTER
        binary_tree[new_node_ptr].right_child = NULL_POINTER

        # Check if the tree is empty
        if root == NULL_POINTER:
            # Insert the new node as the root node
            root = new_node_ptr
        else:
            # Find the insertion point for the new node in the tree
            this_node_ptr = root # Start at the root of the tree
            while this_node_ptr != NULL_POINTER:
                # While not a leaf node
                previous_node_ptr = this_node_ptr # Remember the current node
                if binary_tree[this_node_ptr].data > new_item:
                    # Follow the left pointer if the current node's data is greater than the new item
                    turned_left = True
                    this_node_ptr = binary_tree[this_node_ptr].left_child
                else:
                    # Follow the right pointer if the current node's data is less than or equal to the new item
                    turned_left = False
                    this_node_ptr = binary_tree[this_node_ptr].right_child

            # Insert the new node as the left or right child of the previous node, depending on the value of turned_left
            if turned_left:
                binary_tree[previous_node_ptr].left_child = new_node_ptr
            else:
                binary_tree[previous_node_ptr].right_child = new_node_ptr
    else:
        print("Error: The binary tree is full. Cannot insert a new node.")

# Iteratively search for a node in the tree
def iterative_search(search_item):
    global root, binary_tree

    this_node_ptr = root  # Start at the root of the tree
    while this_node_ptr != NULL_POINTER:  # While there is a pointer to follow
        if binary_tree[this_node_ptr].data == search_item:
            # If the search item is found at the current node, return the node pointer
            return this_node_ptr
        elif binary_tree[this_node_ptr].data > search_item:
            # If the current node's data is greater than the search item, follow the left pointer
            this_node_ptr = binary_tree[this_node_ptr].left_child
        else:
            # If the current node's data is less than or equal to the search item, follow the right pointer
            this_node_ptr = binary_tree[this_node_ptr].right_child

    # If the search item is not found, return NULL_POINTER
    return NULL_POINTER

# Recursively search for a node in the tree
def recursive_search(node_ptr, search_item):
    global binary_tree

    if node_ptr == NULL_POINTER or binary_tree[node_ptr].data == search_item:
        # If the current node is NULL_POINTER or the search item is found, return the node pointer
        return node_ptr
    elif binary_tree[node_ptr].data > search_item:
        # If the current node's data is greater than the search item, search the left subtree
        return recursive_search(binary_tree[node_ptr].left_child, search_item)
    else:
        # If the current node's data is less than or equal to the search item, search the right subtree
        return recursive_search(binary_tree[node_ptr].right_child, search_item)

# InOrderTraversal subroutine: Performs an in-order traversal of the binary tree.
# node_ptr: The node pointer to start the traversal from.
def in_order_traversal(node_ptr):
    global binary_tree

    if node_ptr != NULL_POINTER:
        # Traverse the left subtree
        in_order_traversal(binary_tree[node_ptr].left_child)

        # Process the current node (print the data)
        print(binary_tree[node_ptr].data)

        # Traverse the right subtree
        in_order_traversal(binary_tree[node_ptr].right_child)

# Pre-order traversal subroutine: Performs a pre-order traversal of the binary tree.
# NodePtr: The node pointer to start the traversal from.
def pre_order_traversal(node_ptr):
    if node_ptr != NULL_POINTER:
        # Process the current node
        print(binary_tree[node_ptr].data)
        # Traverse the left subtree
        pre_order_traversal(binary_tree[node_ptr].left_child)
        # Traverse the right subtree
        pre_order_traversal(binary_tree[node_ptr].right_child)

# Post-order traversal subroutine: Performs a post-order traversal of the binary tree.
# NodePtr: The node pointer to start the traversal from.
def post_order_traversal(node_ptr):
    if node_ptr != NULL_POINTER:
        # Traverse the left subtree
        post_order_traversal(binary_tree[node_ptr].left_child)
        # Traverse the right subtree
        post_order_traversal(binary_tree[node_ptr].right_child)
        # Process the current node
        print(binary_tree[node_ptr].data)

# Subroutine to show the content of the binary tree array
def show_binary_tree_array():
    print("Root:", root)
    print("Free Pointer:", free_pointer)
    print("Binary Tree Array Content:")
    for index in range(MAX_TREE_SIZE):
        print(f"Index: {index}, Left Child: {binary_tree[index].left_child}, \
            Data: {binary_tree[index].data}, Right Child: {binary_tree[index].right_child}")
initialize_tree()

while True:
    print("Binary Tree Operations Menu:")
    print("1. Insert a node")
    print("2. Search for a node (Iteratively)")
    print("3. Search for a node (Recursively)")
    print("4. In-order traversal")
    print("5. Pre-order traversal")
    print("6. Post-order traversal")
    print("7. Show Binary Tree Array Content")
    print("8. Exit")
    choice = int(input("Enter your choice (1-8): "))

    if choice == 1:
        new_item = input("Enter the item to be inserted: ")
        insert_node(new_item)
    elif choice == 2:
        search_item = input("Enter the item to search for: ")
        node_pointer = iterative_search(search_item)
        if node_pointer == NULL_POINTER:
            print("Item not found.")
        else:
            print("Item found at node pointer:", node_pointer)
    elif choice == 3:
        search_item = input("Enter the item to search for: ")
        recursive_node_pointer = recursive_search(root, search_item)
        if recursive_node_pointer == NULL_POINTER:
            print("Item not found.")
        else:
            print("Item found at node pointer:", recursive_node_pointer)
    elif choice == 4:
        print("In-order traversal:")
        in_order_traversal(root)
        print()
    elif choice == 5:
        print("Pre-order traversal:")
        pre_order_traversal(root)
        print()
    elif choice == 6:
        print("Post-order traversal:")
        post_order_traversal(root)
        print()
    elif choice == 7:
        show_binary_tree_array()
        print()
    elif choice == 8:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 8.")