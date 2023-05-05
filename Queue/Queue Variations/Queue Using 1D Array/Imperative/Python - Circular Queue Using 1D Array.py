"""
This program implements a circular queue using a 1D array.
The queue has a fixed size of 10 elements.
The front and rear pointers are used to keep track of the
elements in the queue.
"""
# Initialize an empty queue list with size 10 and 
# pointers for front and rear
queue = [-1] * 10
front = -1
rear = -1

# Enqueue operation to add an element to the queue
def enqueue(data):
    global front, rear
    # Check if queue is full by checking if the rear pointer is one
    if (rear + 1) % len(queue) == front:
        print("Queue is full\n")
    # If queue is empty, set front and rear pointers to 0
    elif front == -1 and rear == -1:
        front = 0
        rear = 0
        queue[rear] = data
    # If queue is not empty, move the rear pointer to the 
    # next element and add the data to it
    else:
        # rear is incremented in a circular fashion
        rear = (rear + 1) % len(queue)
        queue[rear] = data # Add data to the rear

# Dequeue operation to remove an element from the front of the queue
def dequeue():
    global front, rear
    # Check if queue is empty
    if front == -1 and rear == -1:
        print("Queue is empty\n")
    # If queue has only one element, reset front and rear pointers
    elif front == rear:
        data = queue[front]
        queue[front] = -1
        front = -1
        rear = -1
        return data
    # If queue has more than one element, move the front pointer 
    # to the next element and remove the data from it
    else:
        data = queue[front]
        queue[front] = -1
        # front is incremented in a circular fashion
        front = (front + 1) % len(queue)
        return data

# Display operation to print the elements in the queue
def display():
    global front, rear
    # Check if queue is empty
    if front == -1 and rear == -1:
        print("Queue is empty\n")
    else:
        print("Elements in the queue: ")
        # Iterate through the elements in the queue and 
        # print them out in order
        i = front
        while i != rear:
            print(queue[i], end=" ")
            # i is incremented in a circular fashion
            i = (i + 1) % len(queue) 
        print(queue[rear], end=" ")
        print("\n")
        print("Front:", front)
        print("Rear:", rear)
        # Print the size of the queue by subtracting the front
        # pointer from the rear pointer and adding 1
        # but if there is a wrap around at the end of the queue,
        # then the size is calculated by subtracting the front
        # pointer from the length of the queue and adding the
        # rear pointer to it and adding 1
        if front <= rear:
            print("Size:", rear - front + 1)
        else:
            print("Size:", len(queue) - front + rear + 1)

# Main loop to control the user's interaction with the queue
while True:
    # Print out the menu options
    print("Enter 1 to enqueue an element")
    print("Enter 2 to dequeue an element")
    print("Enter 3 to display the queue")
    print("Enter 4 to exit")
    # Read in the user's choice
    choice = int(input("Enter your choice: "))
    # Perform the selected operation based on the user's choice
    if choice == 1:
        data = int(input("Enter the element to be enqueued: "))
        enqueue(data)
    elif choice == 2:
        data = dequeue()
        if data != None:
            print("The dequeued element is:", data)
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("Invalid choice\n")
