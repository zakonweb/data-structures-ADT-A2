' VB.NET code to implement stack using linked list.
' It uses the concept of LIFO (Last In First Out).
' It has following global pointers: topOfStack, head, free.
' It has following functions: push, pop, displayArray, displayStack.

Module Program
    Public Structure Node
        Public data As Integer
        Public pointer As Integer
    End Structure

    ' Constants
    Const MAX As Integer = 10
    Const NULL_POINTER As Integer = -1

    ' Global Variables
    Dim topOfStack As Integer = NULL_POINTER
    Dim head As Integer = NULL_POINTER
    Dim free As Integer = 0

    ' Stack Array of Nodes
    Dim stack(MAX - 1) As Node

    Sub Main()
        InitializeStack()
        Dim data As Integer
        Dim Choice As Integer = 0

        While Choice <> 5
            Console.WriteLine(vbCrLf & "Stack Using Linked List")
            Console.WriteLine("1. Push")
            Console.WriteLine("2. Pop")
            Console.WriteLine("3. Display Stack")
            Console.WriteLine("4. Print Linked List Array")
            Console.WriteLine("5. Exit")
            Console.Write("Enter your choice: ")
            Choice = Integer.Parse(Console.ReadLine())

            Select Case Choice
                Case 1
                    Console.Write("Enter integer data: ")
                    data = Integer.Parse(Console.ReadLine())
                    Push(data)
                Case 2
                    Dim poppedData As Integer? = Pop()
                    If poppedData.HasValue Then
                        Console.WriteLine("Popped element: " & poppedData.ToString())
                    End If
                Case 3
                    DisplayStack()
                Case 4
                    DisplayArray()
                Case 5
                    Console.WriteLine("Thank You")
                Case Else
                    Console.WriteLine("Invalid Choice")
            End Select
        End While
    End Sub

    ' Function to Initialize the Stack
    Sub InitializeStack()
        topOfStack = NULL_POINTER
        head = NULL_POINTER
        free = 0

        For i As Integer = 0 To MAX - 2
            stack(i).pointer = i + 1
        Next

        stack(MAX - 1).pointer = NULL_POINTER
    End Sub

    ' Function to Push an Element into the Stack
    Sub Push(ByVal data As Integer)
        If free = NULL_POINTER Then
            Console.WriteLine("Stack Overflow")
            Return
        Else
            Dim temp As Integer = free
            free = stack(free).pointer
            stack(temp).data = data
            stack(temp).pointer = topOfStack
            topOfStack = temp

            If head = NULL_POINTER Then
                head = topOfStack
            End If
        End If
    End Sub

    ' Function to Pop an Element from the Stack
    Function Pop() As Integer?
        If topOfStack = NULL_POINTER Then
            Console.WriteLine("Stack Underflow")
            Return Nothing
        Else
            Dim temp As Integer = topOfStack
            topOfStack = stack(topOfStack).pointer
            stack(temp).pointer = free
            free = temp

            If topOfStack = NULL_POINTER Then
                head = NULL_POINTER
            End If

            Dim val As Integer? = stack(temp).data
            stack(temp).data = Nothing
            Return val
        End If
    End Function

    ' Function to Display the Stack
    Sub DisplayStack()
        Dim temp As Integer = topOfStack

        If topOfStack = NULL_POINTER Then
            Console.WriteLine("Stack is Empty")
            Return
        Else
            While temp <> NULL_POINTER
                If temp = topOfStack Then
                    Console.WriteLine(stack(temp).data.ToString() & vbTab & "<---")
                Else
                    Console.WriteLine(stack(temp).data.ToString())
                End If
                temp = stack(temp).pointer
            End While
        End If
    End Sub

    ' Function to Display the Array
    Sub DisplayArray()
        Console.WriteLine("index" & vbTab & "data" & vbTab & "next")
        For i As Integer = 0 To MAX - 1
            Console.Write(i & vbTab & stack(i).data & vbTab & stack(i).pointer)

            If i = free Then
                Console.WriteLine(vbTab & "free")
            ElseIf i = topOfStack Then
                Console.WriteLine(vbTab & "top_of_stack | tail_of_LL")
            ElseIf i = head Then
                Console.WriteLine(vbTab & "head")
            Else
                Console.WriteLine()
            End If
        Next
        Console.WriteLine("top_of_stack: " & topOfStack)
        Console.WriteLine("head: " & head)
        Console.WriteLine("free: " & free)

    End Sub

End Module
' end of program