Module Module1
    Const NULL_POINTER As Integer = -1
    Dim STACK As Integer()
    Dim TOP_OF_STACK As Integer

    Sub Main()
        ' Initialize top of stack to null pointer and prompt user for stack size
        TOP_OF_STACK = NULL_POINTER
        Console.WriteLine("Enter the size of the stack:")
        Dim SIZE As Integer = Integer.Parse(Console.ReadLine())

        ' Initialize stack array with null values
        ReDim STACK(SIZE - 1)

        ' Start menu loop
        While True
            ' Print menu options and prompt user for choice
            Console.WriteLine("1. Push")
            Console.WriteLine("2. Pop")
            Console.WriteLine("3. Display")
            Console.WriteLine("4. Display Array")
            Console.WriteLine("5. Exit")
            Console.Write("Enter your choice: ")
            Dim CHOICE As Integer = Integer.Parse(Console.ReadLine())

            ' Perform selected operation based on user's choice
            Select Case CHOICE
                Case 1
                    Console.Write("Enter the value to push: ")
                    Dim VALUE As Integer = Integer.Parse(Console.ReadLine())
                    PUSH(VALUE)
                Case 2
                    POP()
                Case 3
                    DISPLAY()
                Case 4
                    DISPLAY_ARRAY()
                Case 5
                    ' Exit the program
                    Exit While
                Case Else
                    ' Invalid choice, ask the user to try again
                    Console.WriteLine("Invalid choice. Try again.")
            End Select
        End While
    End Sub

    ' Subroutine to push a value onto the stack
    Sub PUSH(ByVal VALUE As Integer)
        ' Push the value onto the stack
        If TOP_OF_STACK = STACK.Length - 1 Then
            Console.WriteLine("Stack is full. Cannot push value.")
        Else
            TOP_OF_STACK += 1
            STACK(TOP_OF_STACK) = VALUE
        End If
    End Sub

    ' Subroutine to pop the top value from the stack
    Sub POP()
        ' Pop the top value from the stack
        If TOP_OF_STACK = NULL_POINTER Then
            Console.WriteLine("Stack is empty. Cannot pop value.")
        Else
            Dim VALUE As Integer = STACK(TOP_OF_STACK)
            TOP_OF_STACK -= 1
            Console.WriteLine("Popped value is " & VALUE)
        End If
    End Sub

    ' Subroutine to display the stack as a list of values with the pointer at the top
    Sub DISPLAY()
        ' Display the stack as a list of values with the pointer at the top
        If TOP_OF_STACK = NULL_POINTER Then
            Console.WriteLine("Stack is empty. Cannot display value.")
        Else
            Console.WriteLine("Pointer is at " & TOP_OF_STACK)
            For i As Integer = TOP_OF_STACK To 0 Step -1
                Console.WriteLine(STACK(i))
            Next
        End If
    End Sub

    ' Subroutine to display the entire stack array with the pointer value
    Sub DISPLAY_ARRAY()
        ' Display the entire stack array with the pointer value
        If TOP_OF_STACK = NULL_POINTER Then
            Console.WriteLine("Stack is empty. Cannot display value.")
        Else
            Console.WriteLine("Pointer is at " & TOP_OF_STACK)
            For i As Integer = 0 To STACK.Length - 1
                Console.WriteLine("Index " & i & ": " & STACK(i))
            Next
        End If
    End Sub
End Module
