﻿
Module Module1
    'NullPointer should be set to -1 if using array element with index 0
    Const NULLPOINTER = -1

    'Declare record type to store data and pointer
    Structure Node
        Dim Data As String
        Dim Pointer As Integer
    End Structure

    Dim Queue(7) As Node
    Dim HeadOfQueue As Integer
    Dim EndOfQueue As Integer
    Dim FreeListPtr As Integer

    Sub Main()
        Dim Choice As Char
        Dim Data As String
        Dim CurrentNodePtr As Integer
        InitialiseQueue()
        Choice = GetOption()
        Do While Choice <> "4"
            Select Case Choice
                Case "1"
                    Console.Write("Enter the value: ")
                    Data = Console.ReadLine()
                    JoinQueue(Data)
                    OutputAllNodes()
                Case "2"
                    Data = LeaveQueue()
                    Console.WriteLine("Data popped: " & Data)
                    OutputAllNodes()
                Case "3"
                    OutputAllNodes()
                    Console.Write(HeadOfQueue & " " & " " & EndOfQueue & " ")
                    Console.WriteLine(FreeListPtr)
                    For i = 0 To 7
                        Console.Write(i & " " & Queue(i).Data & " ")
                        Console.WriteLine(Queue(i).Pointer)
                    Next
            End Select
            Choice = GetOption()
        Loop
    End Sub

    Sub InitialiseQueue()
        HeadOfQueue = NULLPOINTER ' set start pointer
        EndOfQueue = NULLPOINTER
        FreeListPtr = 0 ' set starting position of free list
        For Index = 0 To 7 'link all nodes to make free list
            Queue(Index).Pointer = Index + 1
        Next
        Queue(7).Pointer = NULLPOINTER 'last node of free list
    End Sub

    Function LeaveQueue() As String
        Dim ThisNodePtr As Integer
        Dim Value As String

        If HeadOfQueue = NULLPOINTER Then
            Console.WriteLine("Empty Queue")
            Value = ""
        Else
            Value = Queue(HeadOfQueue).Data
            ThisNodePtr = Queue(HeadOfQueue).Pointer
            If ThisNodePtr = NULLPOINTER Then
                EndOfQueue = NULLPOINTER
            End If
            Queue(HeadOfQueue).Pointer = FreeListPtr
            FreeListPtr = HeadOfQueue
            HeadOfQueue = ThisNodePtr
        End If
        Return Value
    End Function

    Sub JoinQueue(ByVal NewItem)
        Dim NewNodePtr As Integer

        If FreeListPtr <> NULLPOINTER Then
            'There is space in the array
            'Take node from free list and store data item
            NewNodePtr = FreeListPtr
            Queue(NewNodePtr).Data = NewItem
            FreeListPtr = Queue(FreeListPtr).Pointer
            Queue(NewNodePtr).Pointer = NULLPOINTER

            If EndOfQueue = NULLPOINTER Then
                HeadOfQueue = NewNodePtr
            Else
                Queue(EndOfQueue).Pointer = NewNodePtr
            End If
            EndOfQueue = NewNodePtr
        Else
            Console.WriteLine("no space for more data")
        End If
    End Sub

    Sub OutputAllNodes()
        Dim CurrentNodePtr As Integer
        CurrentNodePtr = HeadOfQueue ' start at beginning of queue

        If HeadOfQueue = NULLPOINTER Then
            Console.WriteLine("No data in queue")
        End If

        Do While CurrentNodePtr <> NULLPOINTER ' while not end of list
            Console.WriteLine(CurrentNodePtr & " " & Queue(CurrentNodePtr).Data)
            ' follow the pointer to the next node
            CurrentNodePtr = Queue(CurrentNodePtr).Pointer
        Loop
    End Sub

    Function GetOption()
        Dim Choice As Char
        Console.WriteLine("1: Join queue")
        Console.WriteLine("2: Leave queue")
        Console.WriteLine("3: Output queue")
        Console.WriteLine("4: End program")
        Console.Write("Enter your choice: ")
        Choice = Console.ReadLine()
        Return (Choice)
    End Function

End Module