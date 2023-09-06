"""
A Ordered Linked List in python using Object Oriented Programming.

A Ordered Linked List is a linked list that maintains its elements in sorted order. This means that when
you insert a new element into a ordered linked list, it is inserted into its correct position in the list.
Similarly, when you delete an element from a ordered linked list, it is removed from its correct position
in the list.

If you do not know what a linked list is, then refer to the README.md file in the folder
"""
import copy

# The Node class is used to represent a single node in a linked list.
class Node:
    def __init__(self, item: int):
        self.data = item
        self.next = None

# The OrderedLinkedList class is a data structure that maintains a sorted list of elements.
class OrderedLinkedList:
    def __init__(self):
        self.head = None

    def insert_item(self, item: int) -> int:
        """
        The function inserts a new node with the given item into a linked list in ascending order.

        :param item: The "item" parameter is an integer value that represents the item to be inserted
        into the linked list
        :type item: int
        :return: an integer.
        """

        current_node = self.head

        if current_node is None:
            new_node = Node(item)
            new_node.next = current_node
            self.head = new_node
            return

        if current_node.data > item:
            new_node = Node(item)
            new_node.next = current_node
            self.head = new_node
            return

        """
        Traverse the ordered linked list to find the correct position to insert the new item.
        Stop when you find a node whose data is greater than the item to be inserted.
        This ensures that the linked list remains ordered.

        For example, if inserting item 4 in the list 1 -> 3 -> 5 -> 7,
        it will stop at the node with data 3 since the node after 3 is > 4 (5 > 4).

        Create a new node with the item to be inserted.
        Set the new node's 'next' pointer to point to the node that used to come after the current node.
        This preserves the order of the linked list.
        For example, if inserting item 4, the new node's 'next' pointer will point to the node with data 5.

        Update the 'next' pointer of the current node to point to the new node.
        This effectively inserts the new node between the current node and the node that used to come after it.
        For example, if inserting item 4, the current node's 'next' pointer will now point to the new node (4).
        """
        while current_node.next is not None:
            if current_node.next.data > item:
                break

            current_node = current_node.next

        new_node = Node(item)
        new_node.next = current_node.next
        current_node.next = new_node
        return


    def remove_item(self, item: int) -> int:
        """
        The function removes the first occurrence of a specified item from a linked list.

        :param item: The "item" parameter is an integer that represents the value of the item to be
        removed from the linked list
        :type item: int
        :return: None.
        """

        current_node = self.head

        if current_node is None:
            return

        if current_node.data == item:
            self.head = current_node.next
            return

        while current_node.next is not None:
            if current_node.next.data == item:
                break

            current_node = current_node.next

        if current_node.next is None:
            return

        current_node.next = current_node.next.next
        return

    def search_item(self, item: int) -> int:
        """
        The function searches for a specific item in a linked list and returns its index if found,
        otherwise returns -1.

        :param item: The "item" parameter is the value that you want to search for in the linked list
        :type item: int
        :return: The search_item function returns the index of the item if it is found in the linked
        list. If the item is not found, it returns -1.
        """
        current_node = copy.deepcopy(self.head)
        index = 0

        while current_node is not None:
            print(current_node.data)
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

li = OrderedLinkedList()
option = 0

while option != 6:
    print("Ordered Linked List Operations")
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