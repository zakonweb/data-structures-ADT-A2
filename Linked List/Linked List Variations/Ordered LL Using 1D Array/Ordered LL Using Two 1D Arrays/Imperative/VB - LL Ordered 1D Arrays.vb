Imports System.Text
Imports System.Text.RegularExpressions

Module linkedList
    ' Constant null pointer
    Dim NULL_POINTER As Integer = -1

    ' Declare global pointers
    Dim head As Integer = NULL_POINTER
    Dim tail As Integer = NULL_POINTER
    Dim free As Integer = NULL_POINTER

    ' Create two lists of 10 elements, data(0) to data(9) and nextNode(0) to nextNode(9)
    Dim data(9) As String
    Dim nextNode(9) As Integer

    ' Initialise the free list
    Sub init_free_list()
        free = 0
        head = NULL_POINTER
        tail = NULL_POINTER
        For i As Integer = 0 To 8 ' 0 to 8
            nextNode(i) = i + 1
        Next
        nextNode(9) = NULL_POINTER
    End Sub

    ' Add a node in ascending order to the list
    Sub add_list_item(item As String)
        Dim temp As Integer = 0

        ' Check if there is an available node
        If free = NULL_POINTER Then
            Console.WriteLine("List is full. Cannot add more items.")
            Return
        End If

        ' Check if the list is empty
        If head = NULL_POINTER Then
            head = free
            tail = free
            free = nextNode(free)
            data(head) = item
            nextNode(head) = NULL_POINTER
            Return
        End If

        ' Check if the item is to be added at the head
        If item < data(head) Then
            temp = nextNode(free)
            data(free) = item
            nextNode(free) = head
            head = free
            free = temp
            Return
        End If

        ' Check if the item is to be added at the tail
        If item > data(tail) Then
            temp = nextNode(free)
            data(free) = item
            nextNode(free) = NULL_POINTER
            nextNode(tail) = free
            tail = free
            free = temp
            Return
        End If

        ' Check if the item is to be added in the middle
        ' Find the node before the insertion point
        Dim current As Integer = head
        While item > data(nextNode(current))
            current = nextNode(current)
        End While

        ' Insert the node
        temp = nextNode(free)
        data(free) = item
        nextNode(free) = nextNode(current)
        nextNode(current) = free
        free = temp
    End Sub
    ' Print the list
    Sub print_list()
        Dim current As Integer = head
        While current <> NULL_POINTER
            Console.Write(data(current) & ", ")
            current = nextNode(current)
        End While
    End Sub

    ' Search an item in the list
    Function search_list_item(item As String) As Integer
        Dim current As Integer = head
        While current <> NULL_POINTER
            If data(current) = item Then
                Return current
            End If
            current = nextNode(current)
        End While
        Return NULL_POINTER
    End Function

    ' Print the data() array and nextNode() array and related pointers
    Sub print_array()
        Console.WriteLine("data() and nextNode() array:")
        Console.WriteLine("index" & vbTab & "data" & vbTab & "nextNode")
        For i As Integer = 0 To 9
            Console.WriteLine(i & vbTab & data(i) & vbTab & nextNode(i))
        Next
        Console.WriteLine()
        Console.WriteLine("head = " & head)
        Console.WriteLine("tail = " & tail)
        Console.WriteLine("free = " & free)
    End Sub

    ' Delete a node from the list
    Sub delete_list_item(item As String)
        Dim current, temp As Integer
        ' Check if the list is empty
        If head = NULL_POINTER Then
            Console.WriteLine("List is empty")
            Return
        End If

        ' Check if the item is to be deleted from the head
        If item = data(head) Then
            temp = head
            head = nextNode(head)
            nextNode(temp) = free
            free = temp
            data(free) = ""
            Return
        End If

        ' Check if the item is to be deleted from the tail
        If item = data(tail) Then
            current = head
            While nextNode(current) <> tail
                current = nextNode(current)
            End While
            nextNode(current) = NULL_POINTER
            nextNode(tail) = free
            free = tail
            tail = current
            data(free) = ""
            Return
        End If

        ' Check if the item is to be deleted from the middle
        current = head
        While item <> data(nextNode(current))
            current = nextNode(current)
            If nextNode(current) = NULL_POINTER Then
                Console.WriteLine("Item not found")
                Return
            End If
        End While

        ' Delete the node
        temp = nextNode(current)
        nextNode(current) = nextNode(nextNode(current))
        nextNode(temp) = free
        free = temp
        data(free) = ""
    End Sub

    ' Main program
    Sub Main()
        init_free_list()
        Dim opt As Integer = 0
        While opt <> 6
            Console.WriteLine("1. Add a node")
            Console.WriteLine("2. Delete a node")
            Console.WriteLine("3. Print the list")
            Console.WriteLine("4. Print the array")
            Console.WriteLine("5. Search an item")
            Console.WriteLine("6. Exit")
            Console.Write("Enter your opt: ")
            opt = Integer.Parse(Console.ReadLine())
            If opt = 1 Then
                Console.Write("Enter the item to be added: ")
                Dim item As String = Console.ReadLine()
                add_list_item(item)
            ElseIf opt = 2 Then
                Console.Write("Enter the item to be deleted: ")
                Dim item As String = Console.ReadLine()
                delete_list_item(item)
            ElseIf opt = 3 Then
                print_list()
                Console.WriteLine()
            ElseIf opt = 4 Then
                print_array()
            ElseIf opt = 5 Then
                Console.Write("Enter the item to search for: ")
                Dim item As String = Console.ReadLine()
                Dim index As Integer = search_list_item(item)
                If index = NULL_POINTER Then
                    Console.WriteLine("Item not found.")
                Else
                    Console.WriteLine("Item found at index " & index)
                End If
            ElseIf opt = 6 Then
                Console.WriteLine("Goodbye!")
            Else
                Console.WriteLine("Invalid opt")
            End If
            Console.WriteLine()
        End While
    End Sub

End Module