import java.util.Scanner;

public class StackProgram {
    private static final int NULL_POINTER = -1;
    private int[] STACK;
    private int TOP_OF_STACK;

    public static void main(String[] args) {
        StackProgram program = new StackProgram();
        program.run();
    }

    public void run() {
        // Initialize top of stack to null pointer and prompt user for stack size
        TOP_OF_STACK = NULL_POINTER;
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the size of the stack:");
        int SIZE = scanner.nextInt();

        // Initialize stack array with null values
        STACK = new int[SIZE];

        // Start menu loop
        while (true) {
            // Print menu options and prompt user for choice
            System.out.println("1. Push");
            System.out.println("2. Pop");
            System.out.println("3. Display");
            System.out.println("4. Display Array");
            System.out.println("5. Exit");
            System.out.print("Enter your choice: ");
            int CHOICE = scanner.nextInt();

            // Perform selected operation based on user's choice
            switch (CHOICE) {
                case 1:
                    System.out.print("Enter the value to push: ");
                    int VALUE = scanner.nextInt();
                    push(VALUE);
                    break;
                case 2:
                    pop();
                    break;
                case 3:
                    display();
                    break;
                case 4:
                    displayArray();
                    break;
                case 5:
                    // Exit the program
                    return;
                default:
                    // Invalid choice, ask the user to try again
                    System.out.println("Invalid choice. Try again.");
            }
        }
    }

    // Subroutine to push a value onto the stack
    public void push(int VALUE) {
        // Push the value onto the stack
        if (TOP_OF_STACK == STACK.length - 1) {
            System.out.println("Stack is full. Cannot push value.");
        } else {
            TOP_OF_STACK++;
            STACK[TOP_OF_STACK] = VALUE;
        }
    }

    // Subroutine to pop the top value from the stack
    public void pop() {
        // Pop the top value from the stack
        if (TOP_OF_STACK == NULL_POINTER) {
            System.out.println("Stack is empty. Cannot pop value.");
        } else {
            int VALUE = STACK[TOP_OF_STACK];
            TOP_OF_STACK--;
            System.out.println("Popped value is " + VALUE);
        }
    }

    // Subroutine to display the stack as a list of values with the pointer at the top
    public void display() {
        // Display the stack as a list of values with the pointer at the top
        if (TOP_OF_STACK == NULL_POINTER) {
            System.out.println("Stack is empty. Cannot display value.");
        } else {
            System.out.println("Pointer is at " + TOP_OF_STACK);
            for (int i = TOP_OF_STACK; i >= 0; i--) {
                System.out.println(STACK[i]);
            }
        }
    }

// Subroutine to display the entire stack array with the pointer value
public void displayArray() {
    // Display the entire stack array with the pointer value
    if (TOP_OF_STACK == NULL_POINTER) {
        System.out.println("Stack is empty. Cannot display value.");
    } else {
        System.out.println("Pointer is at " + TOP_OF_STACK);
        for (int i = 0; i < STACK.length; i++) {
            System.out.println("Index " + i + ": " + STACK[i]);
        }
    }
}
