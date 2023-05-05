Module Module1
    Dim FrontOfQueuePointer, EndOfQueuePointer As Integer
    Const UB = 5
    Const LBound = 0
    Const nullpointer = -1
    Dim FullQ, EmptyQ As Boolean
    Dim Queue(5) As Integer

    Sub Main()
        FrontOfQueuePointer = nullpointer
        EndOfQueuePointer = nullpointer
        FullQ = False
        EmptyQ = True

        Dim choice, value As Integer
        Do
            Console.WriteLine("1. Add to Q")
            Console.WriteLine("2. Delete from Q")
            Console.WriteLine("3. Quit")
            Do
                Console.Write("Enter choice (1..3) ")
                choice = Console.ReadLine
            Loop Until choice >= 1 And choice <= 3

            Select Case choice
                Case 1
                    Console.Write("Enter value to add to Queue: ")
                    value = Console.ReadLine
                    Call addQ(value)
                Case 2
                    value = deleteQ()
                    If value = nullpointer Then
                        Console.WriteLine("Underflow, Item can't be deleted from the Queue.")
                    Else
                        Console.WriteLine("Item deleted = " & value)
                    End If
                    Console.ReadKey()
            End Select
        Loop Until choice = 3
    End Sub

    Sub addQ(ByVal value As Integer)
        If FullQ = True Then
            Console.WriteLine("Overflow, data can't be added to the Queue.")
            Console.ReadKey()
        Else
            If EndOfQueuePointer = UB And FrontOfQueuePointer > nullpointer Then
                EndOfQueuePointer = LBound
            Else
                EndOfQueuePointer += 1
            End If
            Queue(EndOfQueuePointer) = value
            EmptyQ = False
            If EndOfQueuePointer = FrontOfQueuePointer Or _
                (EndOfQueuePointer = UB And _
                 FrontOfQueuePointer = nullpointer) Then
                FullQ = True
            End If
        End If
    End Sub

    Function deleteQ() As Integer
        Dim value As Integer = 0
        If EmptyQ = True Then
            value = (nullpointer)
        Else
            If FrontOfQueuePointer = UB Then
                FrontOfQueuePointer = LBound
            Else
                FrontOfQueuePointer += 1
            End If

            value = Queue(FrontOfQueuePointer)
            FullQ = False
            If FrontOfQueuePointer = EndOfQueuePointer Then
                EmptyQ = True
            End If
        End If
        Return value
    End Function
End Module
