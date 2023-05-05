import java.util.Scanner;

class CircularQueue {
    // Initialize an empty queue array with size 10 and pointers for front and rear
    static int[] queue = new int[10];
    static int front = -1;
    static int rear = -1;

    // Main method to control the user's interaction with the queue
    public static void main(String[] args) {
        // Create a scanner object for user input
        Scanner scanner = new Scanner(System.in);
        // Main loop to display the menu and perform user-selected operations
        while (true) {
            // Print out the menu options
            System.out.println("Enter 1 to enqueue an element");
            System.out.println("Enter 2 to dequeue an element");
            System.out.println("Enter 3 to display the queue");
            System.out.println("Enter 4 to exit");
            // Read in the user's choice
            int choice = scanner.nextInt();
            // Perform the selected operation based on the user's choice
            switch (choice) {
                case 1:
                    System.out.print("Enter the element to be enqueued: ");
                    int data = scanner.nextInt();
                    enqueue(data);
                    break;
                case 2:
                    int dequeuedData = dequeue();
                    if (dequeuedData != -1) {
                        System.out.println("The dequeued element is: " + dequeuedData);
                    }
                    break;
                case 3:
                    display();
                    break;
                case 4:
                    scanner.close();
                    System.exit(0);
                default:
                    System.out.println("Invalid choice");
                    break;
            }
        }
    }

    // Enqueue operation to add an element to the queue
    public static void enqueue(int data) {
        // Check if queue is full by checking if the rear pointer is one
        if ((rear + 1) % queue.length == front) {
            System.out.println("Queue is full");
        }
        // If queue is empty, set front and rear pointers to 0
        else if (front == -1 && rear == -1) {
            front = 0;
            rear = 0;
            queue[rear] = data;
        }
        // If queue is not empty, move the rear pointer to the 
        // next element and add the data to it
        else {
            // rear is incremented in a circular fashion
            rear = (rear + 1) % queue.length;
            queue[rear] = data; // Add data to the rear
        }
    }

    // Dequeue operation to remove an element from the front of the queue
    public static int dequeue() {
        // Check if queue is empty
        if (front == -1 && rear == -1) {
            System.out.println("Queue is empty");
            return -1;
        }
        // If queue has only one element, reset front and rear pointers
        else if (front == rear) {
            int data = queue[front];
            queue[front] = -1;
            front = -1;
            rear = -1;
            return data;
        }
        // If queue has more than one element, move the front pointer 
        // to the next element and remove the data from it
        else {
            int data = queue[front];
            queue[front] = -1;
            // front is incremented in a circular fashion
            front = (front + 1) % queue.length;
            return data;
        }
    }

    // Display operation to print the elements in the queue
    public static void display() {
        // Check if queue is empty
        if (front == -1 && rear == -1) {
            System.out.println("Queue is empty");
        } else {
            System.out.print("Elements in the queue: ");
            // Iterate through the elements in the queue and 
            // print them out in order
            int i = front;
            while (i != rear) {
                System.out.print(queue[i] + " ");
                // i is incremented in a circular fashion
                i = (i + 1) % queue.length;
            }
            System.out.print(queue[rear] + " ");
            System.out.println("\nFront: " + front);
            System.out.println("Rear: " + rear);
            // Print the number of elements in the queue
            // by subtracting the front and rear pointers
            // and adding 1 but if there was a wrap around,
            // add the length of the queue to the difference
            if (rear < front) {
                System.out.println("Elements in the queue: " + (rear - front + queue.length + 1));
            } else
            System.out.println("Elements in the queue: " + (rear - front + 1));
        }
    }
}  // End of class