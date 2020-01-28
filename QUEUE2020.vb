Module Module1

    Dim Queue(8) As Integer
    Const FullQueue = 8
    Const NullPointer = -1
    Dim FrontOfQueuePointer As Integer = NullPointer
    Dim EndOfQueuePointer As Integer = NullPointer

    Sub Main()
        Dim choice, Value As Integer
        Do
            Console.Clear()
            Console.WriteLine("1. Add to Queue.")
            Console.WriteLine("2. Delete from Queue.")
            Console.WriteLine("3. Exit program.")
            Do
                Console.Write("Enter your choice 1..3 : ")
                choice = Console.ReadLine
            Loop Until choice >= 1 And choice <= 3

            Select Case choice
                Case 1 : Call addQ()
                Case 2
                    Value = deleteQ()
                    If Value = -1 Then
                        Console.WriteLine("Underflow, Queue is empty. No value to delete.")
                        Console.ReadKey()
                    Else
                        Console.WriteLine("Queue value deleted = " & Value)
                        Console.ReadKey()
                    End If
            End Select
        Loop Until choice = 3

    End Sub

    Sub addQ()
        If EndOfQueuePointer = FullQueue Then
            If FrontOfQueuePointer = -1 Then
                Console.WriteLine("Overflow, Value can't be added anymore.")
                Console.ReadKey()
            Else
                Call Adjuster()
                Call addQValue()
            End If
        Else
            Call addQValue()
        End If
    End Sub

    Sub addQValue()
        Dim Value As Integer
        Console.Write("Enter Value to Q: ") : Value = Console.ReadLine
        EndOfQueuePointer = EndOfQueuePointer + 1
        Queue(EndOfQueuePointer) = Value
    End Sub

    Sub Adjuster()
        Dim i As Integer
        While FrontOfQueuePointer <> NullPointer
            For i = FrontOfQueuePointer To EndOfQueuePointer - 1
                Queue(i) = Queue(i + 1)
            Next
            FrontOfQueuePointer = FrontOfQueuePointer - 1
            EndOfQueuePointer = EndOfQueuePointer - 1
        End While
    End Sub

    Function deleteQ() As Integer
        Dim Value As Integer
        If FrontOfQueuePointer = EndOfQueuePointer Then
            Value = NullPointer
        Else
            FrontOfQueuePointer = FrontOfQueuePointer + 1
            Value = Queue(FrontOfQueuePointer)
        End If
        Return Value
    End Function
End Module
