Module Module1
    Dim Stack(8) As Integer
    Const FullStack = 8
    Const BaseOfStackPointer = 0
    Dim TopOfStackPointer = -1
    Const NullPointer = -1

    Sub Main()
        Dim choice, Value As Integer
        Do
            Console.Clear()
            Console.WriteLine("1. Push to stack.")
            Console.WriteLine("2. Pop from stack.")
            Console.WriteLine("3. Exit program.")
            Do
                Console.Write("Enter your choice 1..3 : ")
                choice = Console.ReadLine
            Loop Until choice >= 1 And choice <= 3

            Select Case choice
                Case 1 : Call Push()
                Case 2
                    Value = Pop()
                    If Value = -1 Then
                        Console.WriteLine("Underflow, Stack is empty. No value to pop.")
                        Console.ReadKey()
                    Else
                        Console.WriteLine("Stack Value Poped : " & Value)
                        Console.ReadKey()
                    End If
            End Select
        Loop Until choice = 3

    End Sub

    Sub Push()
        Dim Value As Integer
        If TopOfStackPointer = FullStack Then
            Console.WriteLine("Overflow, Stack is full. No more value can be added.")
            Console.ReadKey()
        Else
            Console.Write("Enter value to add to stack: ")
            Value = Console.ReadLine
            TopOfStackPointer = TopOfStackPointer + 1
            Stack(TopOfStackPointer) = Value
        End If
    End Sub

    Function Pop() As Integer
        Dim Value As Integer
        If TopOfStackPointer = NullPointer Then
            Value = NullPointer
        Else
            Value = Stack(TopOfStackPointer)
            TopOfStackPointer = TopOfStackPointer - 1
        End If

        Return Value
    End Function
End Module
