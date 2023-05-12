# complete non-object-oriented code using parallel arrays instead of the node class

# Constant null pointer
NULL_POINTER = -1

# Declare global pointers
head = NULL_POINTER
tail = NULL_POINTER
free = NULL_POINTER

# Create two lists of 10 elements, data[0] to data[9] and next[0] to next[9]
data = [''] * 10
next = [NULL_POINTER] * 10

# Initialise the free list
def init_free_list():
    global free, head, tail
    free = 0
    head = NULL_POINTER
    tail = NULL_POINTER
    for i in range(9):  # 0 to 8
        next[i] = i + 1
    next[9] = NULL_POINTER 

# Add a node in ascending order to the list
def add_list_item(item):
    global head, tail, free

    # Check if there is an available node
    if free == NULL_POINTER:
        print("List is full. Cannot add more items.")
        return

    # Check if the list is empty
    if head == NULL_POINTER:
        head = free
        tail = free
        free = next[free]
        data[head] = item
        next[head] = NULL_POINTER
        return

    # Check if the item is to be added at the head
    if item < data[head]:
        temp = next[free]
        data[free] = item
        next[free] = head
        head = free
        free = temp
        return

    # Check if the item is to be added at the tail
    if item > data[tail]:
        temp = next[free]
        data[free] = item
        next[free] = NULL_POINTER
        next[tail] = free
        tail = free
        free = temp
        return

    # Check if the item is to be added in the middle
    # Find the node before the insertion point
    current = head
    while item > data[next[current]]:
        current = next[current]

    # Insert the node
    temp = next[free]
    data[free] = item
    next[free] = next[current]
    next[current] = free
    free = temp

# Print the list
def print_list():
    current = head
    while current != NULL_POINTER:
        print(data[current], end=', ')
        current = next[current]
    print()

# Search an item in the list
def search_list_item(item):
    current = head
    while current != NULL_POINTER:
        if data[current] == item:
            return current
        current = next[current]
    return NULL_POINTER

# Print the data[] and next[] arrays and related pointers
def print_array():
    print('Array:')
    print('index\tdata\tnext')
    for i in range(10):
        print(i, '\t', data[i], '\t', next[i])
    print()
    print('head = ', head)
    print('tail = ', tail)
    print('free = ', free)

# Delete a node from the list
def delete_list_item(item):
    global head, tail, free

    # Check if the list is empty
    if head == NULL_POINTER:
        print('List is empty')
        return

    # Check if the item is to be deleted from the head
    if item == data[head]:
        temp = head
        head = next[head]
        next[temp] = free
        free = temp
        data[free] = ''
        return
    # Check if the item is to be deleted from the tail
    if item == data[tail]:
        current = head
        while next[current] != tail:
            current = next[current]
        next[current] = NULL_POINTER
        next[tail] = free
        free = tail
        tail = current
        data[free] = ''
        return

    # Check if the item is to be deleted from the middle
    current = head
    while item != data[next[current]]:
        current = next[current]
        if next[current] == NULL_POINTER:
            print('Item not found')
            return

    # Delete the node
    temp = next[current]
    next[current] = next[next[current]]
    next[temp] = free
    free = temp
    data[free] = ''

# Main program
init_free_list()
option = 0
while option != 6:
    print('1. Add a node')
    print('2. Delete a node')
    print('3. Print the list')
    print('4. Print the array')
    print('5. Search an item')
    print('6. Exit')
    option = int(input('Enter your option: '))
    if option == 1:
        item = input('Enter the item to be added: ')
        add_list_item(item)
    elif option == 2:
        item = input('Enter the item to be deleted: ')
        delete_list_item(item)
    elif option == 3:
        print_list()
    elif option == 4:
        print_array()
    elif option == 5:
        item = input('Enter the item to search for: ')
        index = search_list_item(item)
        if index == NULL_POINTER:
            print("Item not found.")
        else:
            print("Item found at index", index)
    elif option == 6:
        print('Goodbye!')
    else:
        print('Invalid option')
    print()

