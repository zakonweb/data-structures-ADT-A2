"""
writing python code for an ordered linked list, lst[].
lst[] will be made up of nodes, that has two attributes, data and next.
list will have a head, tail and a free list pointers
list will be initialised as a free list od connectd nodes
"""

# constant null pointer
NULL_POINTER = -1

# declare the node class
class node():
    def __init__(self):
        self.data = ''
        self.next = NULL_POINTER

# declare global pointers
head = NULL_POINTER
tail = NULL_POINTER
free = NULL_POINTER

# create a list of 10 nodes, lst[0] to lst[9]
lst = [node() for i in range(10)]

# initialise the free list
def init_free_list():
    global free, head, tail
    free = 0
    head = NULL_POINTER
    tail = NULL_POINTER
    for i in range(9):  # 0 to 8
        lst[i].next = i + 1
    lst[9].next = NULL_POINTER 

# add a node in ascending order to the list
def add_list_item(item):
    global head, tail, free

    # Check if there is an available node
    if free == NULL_POINTER:
        print("List is full. Cannot add more items.")
        return

    # check if the list is empty
    if head == NULL_POINTER:
        head = free
        tail = free
        free = lst[free].next
        lst[head].data = item
        lst[head].next = NULL_POINTER
        return

    # check if the item is to be added at the head
    if item < lst[head].data:
        temp = lst[free].next
        lst[free].data = item
        lst[free].next = head
        head = free
        free = temp
        return

    # check if the item is to be added at the tail
    if item > lst[tail].data:
        temp = lst[free].next
        lst[free].data = item
        lst[free].next = NULL_POINTER
        lst[tail].next = free
        tail = free
        free = temp
        return

    # check if the item is to be added in the middle
    # find the node before the insertion point
    current = head
    while item > lst[lst[current].next].data:
        current = lst[current].next

    # insert the node
    temp = lst[free].next
    lst[free].data = item
    lst[free].next = lst[current].next
    lst[current].next = free
    free = temp

# print the list
def print_list():
    current = head
    while current != NULL_POINTER:
        print(lst[current].data, end=', ')
        current = lst[current].next

def search_list_item(item):
    current = head
    while current != NULL_POINTER:
        if lst[current].data == item:
            return current
        current = lst[current].next
    return NULL_POINTER

# print the lst[] array and related pointers
def print_array():
    print('lst[] array:')
    print('index\tdata\tnext')
    for i in range(10):
        print(i, '\t', lst[i].data, '\t', lst[i].next)
    print()
    print('head = ', head)
    print('tail = ', tail)
    print('free = ', free)

# delete a node from the list
def delete_list_item(item):
    global head, tail, free

    # check if the list is empty
    if head == NULL_POINTER:
        print('List is empty')
        return

    # check if the item is to be deleted from the head
    if item == lst[head].data:
        temp = head
        head = lst[head].next
        lst[temp].next = free
        free = temp
        lst[free].data = ''
        return

    # check if the item is to be deleted from the tail
    if item == lst[tail].data:
        current = head
        while lst[current].next != tail:
            current = lst[current].next
        lst[current].next = NULL_POINTER
        lst[tail].next = free
        free = tail
        tail = current
        lst[free].data = ''
        return

    # check if the item is to be deleted from the middle
    current = head
    while item != lst[lst[current].next].data:
        current = lst[current].next
        if lst[current].next == NULL_POINTER:
            print('Item not found')
            return

    # delete the node
    temp = lst[current].next
    lst[current].next = lst[lst[current].next].next
    lst[temp].next = free
    free = temp
    lst[free].data = ''

# main program
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
        print()
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