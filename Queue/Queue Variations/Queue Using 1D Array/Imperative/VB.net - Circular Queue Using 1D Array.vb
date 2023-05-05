Module Module1
    ' Initialize an empty queue array with size 10 and pointers for front and rear
    Dim queue(9) As Integer
    Dim front As Integer = -1
    Dim rear As Integer = -1

    ' Enqueue operation to add an element to the queue
    Sub Enqueue(ByVal data As Integer)
        ' Check if queue is full by checking if the rear pointer is one
        If (rear + 1) Mod queue.Length = front Then
            Console.WriteLine("Queue is full")
            ' If queue is empty, set front and rear pointers to 0
        ElseIf front = -1 And rear = -1 Then
            front = 0
            rear = 0
            queue(rear) = data
            ' If queue is not empty, move the rear pointer to the 
            ' next element and add the data to it
        Else
            ' rear is incremented in a circular fashion
            rear = (rear + 1) Mod queue.Length
            queue(rear) = data ' Add data to the rear
        End If
    End Sub

    ' Dequeue operation to remove an element from the front of the queue
    Function Dequeue() As Integer
        Dim data As Integer
        ' Check if queue is empty
        If front = -1 And rear = -1 Then
            Console.WriteLine("Queue is empty")
            Return -1
            ' If queue has only one element, reset front and rear pointers
        ElseIf front = rear Then
            Data = queue(front)
            queue(front) = -1
            front = -1
            rear = -1
            Return Data
            ' If queue has more than one element, move the front pointer 
            ' to the next element and remove the data from it
        Else
            data = queue(front)
            queue(front) = -1
            ' front is incremented in a circular fashion
            front = (front + 1) Mod queue.Length
            Return data
        End If
    End Function

    ' Display operation to print the elements in the queue
    Sub Display()
        Dim i As Integer
        ' Check if queue is empty
        If front = -1 And rear = -1 Then
            Console.WriteLine("Queue is empty")
        Else
            Console.Write("Elements in the queue: ")
            ' Iterate through the elements in the queue and 
            ' print them out in order
            i = front
            While i <> rear
                Console.Write(queue(i) & " ")
                ' i is incremented in a circular fashion
                i = (i + 1) Mod queue.Length
            End While
            Console.Write(queue(rear) & " ")
            Console.WriteLine()
            Console.WriteLine("Front: " & front)
            Console.WriteLine("Rear: " & rear)
            ' Print the size of the queue by subtracting the front
            ' pointer from the rear pointer and adding 1
            ' but if there is a wrap around at the end of the queue,
            ' then the size is calculated by subtracting the front
            ' pointer from the length of the queue and adding the
            ' rear pointer to it and adding 1
            If front <= rear Then
                Console.WriteLine("Size: " & (rear - front + 1))
            Else
                Console.WriteLine("Size: " & (queue.Length - front + rear + 1))
            End If
        End If
    End Sub

    Sub Main()
        ' Main loop to control the user's interaction with the queue
        Dim choice, data As Integer
        choice = 0
        While True
            ' Print out the menu options
            Console.WriteLine("Enter 1 to enqueue an element")
            Console.WriteLine("Enter 2 to dequeue an element")
            Console.WriteLine("Enter 3 to display the queue")
            Console.WriteLine("Enter 4 to exit")
            ' Read in the user's choice
            Console.Write("Enter your choice: ")
            choice = Console.ReadLine()
            ' Perform the selected operation based on the user's choice
            Select Case choice
                Case 1
                    Console.Write("Enter the element to be enqueued: ")
                    data = Console.ReadLine()
                    Enqueue(data)
                Case 2
                    data = Dequeue()
                    If data <> -1 Then
                        Console.WriteLine("The dequeued element is: " & data)
                    End If
                Case 3
                    Call Display()
                Case 4
                    Exit While
                Case Else
                    Console.WriteLine("Invalid choice")
            End Select
        End While
    End Sub
End Module