"""
This program implements a circular queue using linked list
with free list. It uses a list of nodes to store the elements
of the queue. The nodes are linked together using the next
pointer. The free list is a linked list of nodes that are
currently not being used. The free list is used to avoid
fragmentation of the list of nodes and keep the wrap around
operation simple.
"""

# Node class to store the data and the next pointer
class Node:
    def __init__(self, data=None, next_pointer=-1):
        self.data = data
        self.next_pointer = next_pointer

# Maximum number of nodes in the list
MAX = 10
# NULL pointer to indicate the end of the list
NULL_POINTER = -1

# Global variables
queue_front = NULL_POINTER # Points to the front of the queue
queue_rear = NULL_POINTER # Points to the rear of the queue
free_list_head = 0 # Points to the head of the free list

# List of nodes
node_list = [Node() for _ in range(MAX)]

# Initialize the list of nodes
def initialize_nodes():
    for i in range(MAX - 1): # connect the nodes in the free list
        node_list[i].next_pointer = i + 1
    
    # Set the next pointer of the last node to NULL_POINTER
    node_list[MAX - 1].next_pointer = NULL_POINTER

# Enqueue an element into the queue
def enqueue(data):
    global queue_front, queue_rear, free_list_head

    # Check if the free list is empty
    if free_list_head == NULL_POINTER:
        print("Queue is full")
    else: # Add the element to the rear of the queue
        # Remove the node at the head of the free list
        new_node_index = free_list_head
        # Update the head of the free list
        free_list_head = node_list[free_list_head].next_pointer

        # Add the node to the rear of the queue
        node_list[new_node_index].data = data
        # Set the next pointer of the node to NULL_POINTER
        node_list[new_node_index].next_pointer = NULL_POINTER

        # Check if the queue is empty
        if queue_rear == NULL_POINTER:
            # Set the front and rear pointers to the new node
            queue_front = new_node_index
            queue_rear = new_node_index
        else: # Add the node to the rear of the queue
            node_list[queue_rear].next_pointer = new_node_index
            queue_rear = new_node_index

# Dequeue an element from the queue
def dequeue():
    global queue_front, queue_rear, free_list_head

    # Check if the queue is empty
    if queue_front == NULL_POINTER:
        print("Queue is empty")
        return -1 # Return -1 to indicate an error
    else: # Remove the element from the front of the queue
        old_front_index = queue_front
        # Update the front pointer
        queue_front = node_list[queue_front].next_pointer

        # Check if the queue is empty
        if queue_front == NULL_POINTER:
            queue_rear = NULL_POINTER

        # Add the node to the head of the free list
        node_list[old_front_index].next_pointer = free_list_head
        free_list_head = old_front_index

        # Return the dequeued element
        return node_list[old_front_index].data

# Display the elements in the queue
def display():
    # Check if the queue is empty
    if queue_front == NULL_POINTER:
        print("Queue is empty")
    else: # Display the elements in the queue
        print("Elements in the queue:", end=" ")

        # Start from the front of the queue
        current_index = queue_front
        while current_index != NULL_POINTER:
            print(node_list[current_index].data, end=" ")
            current_index = node_list[current_index].next_pointer
        print()

        # Display the pointers & the size of the current queue
        print("Front pointer:", queue_front)
        print("Rear pointer:", queue_rear)
        print("Free list head:", free_list_head)

        # calculate the size of the current queue
        # and display it
        current_pointer = queue_front
        count = 0
        while current_pointer != NULL_POINTER:
            count += 1
            current_pointer = node_list[current_pointer].next_pointer
        print("Current queue size:", count)

# Initialize the list of nodes
initialize_nodes()

# Main menu program
while True:
    print("\nCircular Queue using Linked List with Free List")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter the element to be enqueued: "))
        enqueue(data)
    elif choice == 2:
        data = dequeue()
        if data != -1:
            print("The dequeued element is:", data)
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("Invalid choice")
# end of the program