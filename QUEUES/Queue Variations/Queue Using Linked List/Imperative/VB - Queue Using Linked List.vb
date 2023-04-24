Module Module1
    'This implementation uses a linked list With a free list
    'To manage nodes efficiently. It consists of a Structure Node
    'that stores the data And a pointer To the Next node.
    'The circular queue Is maintained Using two pointers
    Public Structure Node
        Public Data As Integer
        Public NextPointer As Integer
    End Structure

    Const MAX As Integer = 10
    Const NULL_POINTER As Integer = -1

    Dim QueueFront As Integer = NULL_POINTER
    Dim QueueRear As Integer = NULL_POINTER
    Dim FreeListHead As Integer = 0

    Dim NodeList(MAX - 1) As Node

    Sub Main()
        InitializeNodes()

        Dim Choice As Integer
        Dim Data As Integer

        While True
            Console.WriteLine("Circular Queue using Linked List with Free List")
            Console.WriteLine("1. Enqueue")
            Console.WriteLine("2. Dequeue")
            Console.WriteLine("3. Display")
            Console.WriteLine("4. Exit")
            Console.Write("Enter your choice: ")
            Choice = Integer.Parse(Console.ReadLine())

            Select Case Choice
                Case 1
                    Console.Write("Enter the element to be enqueued: ")
                    Data = Integer.Parse(Console.ReadLine())
                    Enqueue(Data)
                Case 2
                    Data = Dequeue()
                    If Data <> -1 Then
                        Console.WriteLine("The dequeued element is: " & Data)
                    End If
                Case 3
                    Display()
                Case 4
                    Exit While
                Case Else
                    Console.WriteLine("Invalid choice")
            End Select
        End While
    End Sub

    Sub InitializeNodes()
        For i As Integer = 0 To MAX - 2
            NodeList(i).NextPointer = i + 1
        Next

        NodeList(MAX - 1).NextPointer = NULL_POINTER
    End Sub

    Sub Enqueue(ByVal Data As Integer)
        If FreeListHead = NULL_POINTER Then
            Console.WriteLine("Queue is full")
        Else
            Dim NewNodeIndex As Integer = FreeListHead
            FreeListHead = NodeList(FreeListHead).NextPointer

            NodeList(NewNodeIndex).Data = Data
            NodeList(NewNodeIndex).NextPointer = NULL_POINTER

            If QueueRear = NULL_POINTER Then
                QueueFront = NewNodeIndex
                QueueRear = NewNodeIndex
            Else
                NodeList(QueueRear).NextPointer = NewNodeIndex
                QueueRear = NewNodeIndex
            End If
        End If
    End Sub

    Function Dequeue() As Integer
        If QueueFront = NULL_POINTER Then
            Console.WriteLine("Queue is empty")
            Return -1
        Else
            Dim OldFrontIndex As Integer = QueueFront
            QueueFront = NodeList(QueueFront).NextPointer

            If QueueFront = NULL_POINTER Then
                QueueRear = NULL_POINTER
            End If

            NodeList(OldFrontIndex).NextPointer = FreeListHead
            FreeListHead = OldFrontIndex

            Return NodeList(OldFrontIndex).Data
        End If
    End Function

    Sub Display()
        Dim Size As Integer = 0 'variable to store the size of the queue
        If QueueFront = NULL_POINTER Then
            Console.WriteLine("Queue is empty")
        Else
            Console.Write("Elements in the queue: ")

            Dim CurrentIndex As Integer = QueueFront
            While CurrentIndex <> NULL_POINTER
                Console.Write(NodeList(CurrentIndex).Data & " ")
                CurrentIndex = NodeList(CurrentIndex).NextPointer
            End While
            Console.WriteLine()

            ' Display pointer values and number of elements in the queue
            Console.WriteLine("fornt: " & QueueFront)
            Console.WriteLine("rear: " & QueueRear)
            Console.WriteLine("free: " & FreeListHead)
            'Calculate the size of the queue
            CurrentIndex = QueueFront
            While CurrentIndex <> NULL_POINTER
                Size += 1
                CurrentIndex = NodeList(CurrentIndex).NextPointer
            End While
            Console.WriteLine("Size: " & Size)

            Console.WriteLine()
        End If
    End Sub
End Module
