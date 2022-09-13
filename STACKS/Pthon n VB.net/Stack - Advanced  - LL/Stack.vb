Module Module1
    ' NullPointer should be set to -1 if using array element with index 0
    Const NULLPOINTER = -1
    ' Declare record type to store data and pointer

    Structure Node
        Dim Data As String
        Dim Pointer As Integer
    End Structure

    Dim Stack(7) As Node
    Dim TopOfStack As Integer
    Dim FreeListPtr As Integer

    Sub Main()
        Dim Choice As Char
        Dim Data As String
        Dim CurrentNodePtr As Integer
        InitialiseStack()
        Choice = GetOption()
        Do While Choice <> "4"
            Select Case Choice
                Case "1"
                    Console.Write("Enter the value: ")
                    Data = Console.ReadLine()
                    Push(Data)
                    OutputAllNodes()
                Case "2"
                    Data = Pop()
                    Console.WriteLine("Data popped: " & Data)
                    OutputAllNodes()
                Case "3"
                    OutputAllNodes()
                    Console.WriteLine(TopOfStack & " " & FreeListPtr)
                    For i = 1 To 7
                        Console.WriteLine(i & " " & Stack(i).Data & " " & Stack(i).Pointer)
                    Next
            End Select
            Choice = GetOption()
        Loop
    End Sub

    Sub InitialiseStack()
        TopOfStack = NULLPOINTER ' set start pointer
        FreeListPtr = 0 ' set starting position of free list
        For Index = 0 To 7 'link all nodes to make free list

            Stack(Index).Pointer = Index + 1
        Next
        Stack(7).Pointer = NULLPOINTER 'last node of free list
    End Sub

    Function Pop()
        Dim ThisNodePtr As Integer
        Dim Value As String
        If TopOfStack = NULLPOINTER Then
            Console.WriteLine("no data on stack")
            Value = ""
        Else
            Value = Stack(TopOfStack).Data
            ThisNodePtr = TopOfStack
            TopOfStack = Stack(TopOfStack).Pointer
            Stack(ThisNodePtr).Pointer = FreeListPtr
            FreeListPtr = ThisNodePtr
        End If
        Return Value
    End Function

    Sub Push(ByVal NewItem)
        Dim NewNodePtr As Integer
        If FreeListPtr <> NULLPOINTER Then
            ' there is space in the array
            ' take node from free list and store data item
            NewNodePtr = FreeListPtr
            Stack(NewNodePtr).Data = NewItem
            FreeListPtr = Stack(FreeListPtr).Pointer
            ' insert new node at top of stack
            Stack(NewNodePtr).Pointer = TopOfStack
            TopOfStack = NewNodePtr
        Else
            Console.WriteLine("no space for more data")
        End If
    End Sub

    Sub OutputAllNodes()
        Dim CurrentNodePtr As Integer
        CurrentNodePtr = TopOfStack ' start at beginning of list
        If TopOfStack = NULLPOINTER Then
            Console.WriteLine("No data on stack")
        End If
        Do While CurrentNodePtr <> NULLPOINTER ' while not end of list
            Console.WriteLine(CurrentNodePtr & " " & Stack(CurrentNodePtr).Data)
            ' follow the pointer to the next node
            CurrentNodePtr = Stack(CurrentNodePtr).Pointer
        Loop
    End Sub

    Function GetOption()
        Dim Choice As Char
        Console.WriteLine("1: Push a value")
        Console.WriteLine("2: Pop a value")
        Console.WriteLine("3: Output stack")
        Console.WriteLine("4: End program")
        Console.Write("Enter your choice: ")
        Choice = Console.ReadLine()
        Return (Choice)
    End Function

End Module