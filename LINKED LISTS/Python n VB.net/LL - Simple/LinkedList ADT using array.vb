Module Module1

    Structure LinkedList
        Dim Data As String
        Dim Pointer As Integer
    End Structure

    Dim List1(11) As LinkedList
    Dim d As String
    Dim Free As Integer = 0
    Dim Temp, Temp2 As Integer
    Dim Current As Integer
    Dim ListStart = 0

    Sub Main()
        Dim MenuOption As Integer
        Call listInitialise()

        Do
            Console.WriteLine("1. Add item to list.")
            Console.WriteLine("2. Delete item from list.")
            Console.WriteLine("3. Display items in list.")
            Console.WriteLine("4. Search item in List.")
            Console.WriteLine("0. Quit.")
            Console.WriteLine()
            Console.Write("Enter your choice.....")
            MenuOption = Console.ReadLine

            Select Case MenuOption
                Case 1 : ListAdd()
                Case 2 : listDelete()
                Case 3 : ListDisplay()
                Case 4 : ListSearch()
            End Select

        Loop Until MenuOption = 0

    End Sub

    Sub listInitialise()
        Dim i As Integer
        For i = 0 To 11
            List1(i).Data = ""
            List1(i).Pointer = -1
        Next
    End Sub

    Sub ListDisplay()
        Dim a As Integer
        For a = 0 To 11
            Console.WriteLine(a & ".      " & List1(a).Data & " : " & List1(a).Pointer)
        Next
        Console.ReadKey()
    End Sub

    Sub ListAdd()
        Console.Write("Enter item to add.....")
        d = Console.ReadLine()

        If Free = -1 Then
            Console.WriteLine("OverFlow")
        Else
            If Free = 0 Then
                List1(Free).Data = d
                ListStart = Free
                IIf(List1(Free).Pointer = -1, Free = Free + 1, Free = List1(Free).Pointer)
                If Free = 12 Then Free = -1
            Else
                If List1(ListStart).Data > d Then
                    List1(Free).Data = d
                    List1(Free).Pointer = ListStart
                    ListStart = Free
                    IIf(List1(Free).Pointer = -1, Free = Free + 1, Free = List1(Free).Pointer)
                    If Free = 12 Then Free = -1
                Else
                    Current = ListStart
                    While List1(List1(Current).Pointer).Data < d

                        Current = List1(Current).Pointer
                        If List1(Current).Pointer = -1 Then Exit While
                    End While
                    List1(Free).Data = d

                    Temp = List1(Current).Pointer
                    List1(Current).Pointer = Free
                    List1(Free).Pointer = Temp
                    IIf(List1(Free).Pointer = -1, Free = Free + 1, Free = List1(Free).Pointer)
                    If Free = 12 Then Free = -1
                End If
            End If
        End If
    End Sub

    Sub listDelete()
        Dim isDeleted As Boolean = False
        d = Console.ReadLine()
        If ListStart = -1 Then
            Console.WriteLine("UnderFlow")
        Else
            isDeleted = False
            Current = ListStart
            While List1(List1(Current).Pointer).Data <> d

                Current = List1(Current).Pointer
                If List1(Current).Pointer = -1 Then Exit While
            End While

            If List1(Current).Pointer <> -1 Then
                Temp = List1(Current).Pointer
                List1(Current).Pointer = List1(List1(Current).Pointer).Pointer
                Temp2 = Free
                Free = Temp
                List1(Free).Pointer = Temp2
                isDeleted = True
            End If

            If isDeleted = False Then
                Console.WriteLine("Data not deleted as it is not found.")
                Console.ReadKey()
            End If
        End If
    End Sub

    Sub ListSearch()
        d = Console.ReadLine()

        Current = ListStart
        While List1(Current).Data <> d Or List1(Current).Pointer <> -1
            Current = List1(Current).Pointer
        End While

        If List1(Current).Data = d Then
            Console.WriteLine("Item Found.")
        Else
            Console.WriteLine("Item Not Found.")
        End If

        Console.ReadKey()
    End Sub
End Module
