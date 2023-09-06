"""
A Unordered Linked List is a linked list that does not maintain its elements in sorted order. This means
that when you insert a new element into a unordered linked list, it is inserted into the front of the list.
Similarly, when you delete an element from a unordered linked list, it is removed from the front of the list.

If you do not know what a linked list is, then refer to the README.md file in the folder
"""

# The Node class is used to represent a single node in a linked list.
class Node:
    def __init__(self, item: int):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_item(self, item):
        """
        The function inserts a new item at the beginning of a linked list.

        :param item: The "item" parameter represents the value of the item that you want to insert into
        the linked list
        """
        current_node = self.head

        node = Node(item)
        node.next = current_node
        self.head = node

    def remove_item(self):
        """
        The function removes the first item in a linked list.
        :return: The method is returning the next node after the current node.
        """
        current_node = self.head

        if current_node is None:
            return

        self.head = current_node.next

    def search_item(self, item):
        """
        The function searches for a specific item in a linked list and returns its index if found,
        otherwise returns -1.

        :param item: The "item" parameter is the value that you want to search for in the linked list
        :return: the index of the item if it is found in the linked list. If the item is not found, it
        returns -1.
        """
        current_node = self.head
        index = 0

        while current_node is not None:
            if current_node.data == item:
                return index

            current_node = current_node.next
            index += 1

        return -1

    """
        The __str__ and __repr__ methods are used to return a string representation of a linked list.
        In Python, the __str__ method is called when you use the print function on an object
        the __repr__ method is called when you use the repr function on an object.
        It is not necessary to use these methods, you can create your own function to print the linked list.
        However, it is recommended to use these methods because they are already implemented in Python.
        And is good practice to use them
    """

    def __str__(self):
        """
        The function returns a string representation of a linked list by iterating through each node and
        appending its data to the output string.
        :return: The method is returning a string representation of the linked list.
        """

        current_node = self.head

        output = ""

        while current_node:
            if current_node.next is None:
                output += str(current_node.data)
                return output

            output += str(current_node.data) + " -> "
            current_node = current_node.next

        return output

    def __repr__(self):
        """
        The above function returns a string representation of a linked list.
        :return: The __repr__ method is returning a string representation of the linked list. It
        iterates through each node in the linked list and appends the data of each node to a list called
        output. Finally, it returns a string representation of the output list, with each element
        separated by a comma and space.
        """

        output = []
        current_node = self.head

        while current_node is not None:
            output.append(current_node.data)
            current_node = current_node.next

        return "[%s]" %(', '.join(str(i) for i in output))

li = LinkedList()
option = 0

while option != 6:
    print("Unordered Linked List Operations")
    print('1. Add a node')
    print('2. Delete a node')
    print('3. Print the list')
    print('5. Search an item')
    print('6. Exit')

    option = int(input('Enter your option: '))

    if option == 1:
        item = input('Enter the item to be added: ')
        li.insert_item(item)

    elif option == 2:
        item = input('Enter the item to be deleted: ')
        li.remove_item(item)

    elif option == 3:
        print(li)

    elif option == 5:
        item = input('Enter the item to search for: ')
        index = li.search_item(item)

        if index == -1:
            print("Item not found.")
        else:
            print("Item found at index", index)

    elif option == 6:

        print('Goodbye!')
    else:
        print('Invalid option')

    print()