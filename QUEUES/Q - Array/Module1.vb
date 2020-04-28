Option Explicit On 'This makes sure all variables that are taken as input are declared
Module Module1
    Dim Queue(9) As String 'Declares an Array of 10 spaces by the name of "Queue" and data type string in the memory
    Dim StartPtr As Integer 'Declares a virtual Start pointer
    Dim EndPtr As Integer 'Declares a virtual End pointer

    Sub Main()
        StartPtr = 0 'Initializes the Start Pointer
        EndPtr = 0 'Initializes the End Pointer
        Dim MenuChoice As Integer = 0
        Do While MenuChoice <> 4
            Console.WriteLine("1. To PUSH to QUEUE")
            Console.WriteLine("2. To POP from QUEUE")
            Console.WriteLine("3. To RESET the QUEUE.")
            Console.WriteLine("4. To exit this module.")
            MenuChoice = Console.ReadLine
            Select Case MenuChoice
                Case 1 : cmdPush_Click()
                Case 2 : cmdPop_Click()
                Case 3 : cmdReset_Click()
                Case 4
                Case Else : Console.WriteLine("Wrong choice. Please try again.")
            End Select
        Loop
    End Sub

    Private Sub cmdPop_Click() 'This command is used to retrieve data from the queue
        If StartPtr = EndPtr Then 'Checks if End pointer and Start pointer are in same location in which case the queue will be empty
            Console.WriteLine("Underflow") 'Displays Error message, stating that queue is empty
            Exit Sub 'Exits the private sub if error is detected
        End If
        Console.WriteLine(Queue(EndPtr)) 'Retrieves value from queue and displays it
        EndPtr = EndPtr + 1 'Moves End Pointer to the next value stored in the queue
    End Sub

    Private Sub cmdPush_Click() 'This command is used to enter data into the queue
        Dim newVal As String 'Declares a variable that is to be input into the queue
        Console.WriteLine("Enter New Value")
        newVal = Console.ReadLine 'Takes the value that is to be input in the queue
        If StartPtr > 9 Then 'Checks if there is space in the queue for more data
            Console.WriteLine("Overflow") 'Displays error message, stating the queue is full
            Exit Sub 'Exits the private sub if error is detected
        End If
        Queue(StartPtr) = newVal 'Stores the value that was input into the queue
        StartPtr = StartPtr + 1 'Moves Start POinter to the next available space in the queue
    End Sub

    Private Sub cmdReset_Click() 'This command is used to reset the queue and to make space available again
        StartPtr = 0 'Initializes the Start Pointer back to its original position
        EndPtr = 0 'Initialized the End Pointer back to its original position
    End Sub
End Module
