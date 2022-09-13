Module BinaryTreeAddition

    Structure binaryTree
        Dim data As String
        Dim left As Integer
        Dim right As Integer
    End Structure

    Dim BT(10) As binaryTree

    Sub Main()
        Dim myVal As String = ""
        Dim i As Integer
        Console.WriteLine("ONLY ENTER UNIQUE VALUES")
        For i = 1 To 10
            Console.Write("Enter Val to Insert to BT :") : myVal = Console.ReadLine
            Call Insert(myVal)
        Next

        Call showBT()
        Console.ReadKey()

    End Sub
    Sub Insert(ByVal val As String)
        Dim isInserted As Boolean = False
        Dim Pos, N As Integer
        Pos = 1
        While isInserted = False
            If BT(Pos).left = 0 And BT(Pos).right = 0 And BT(Pos).data = "" Then
                isInserted = True
                BT(Pos).data = val
                Exit While
            End If

            If val < BT(Pos).data And BT(Pos).data <> Nothing Then
                If BT(Pos).left = 0 Then
                    N = Pos
                    While BT(N).data <> ""
                        N = N + 1
                    End While
                    If N > 10 Then Exit Sub
                    BT(Pos).left = N
                Else
                    Pos = BT(Pos).left
                End If
            End If

            If val > BT(Pos).data And BT(Pos).data <> Nothing Then
                If BT(Pos).right = 0 Then
                    N = Pos
                    While BT(N).data <> ""
                        N = N + 1
                    End While
                    If N > 10 Then Exit Sub
                    BT(Pos).right = N
                Else
                    Pos = BT(Pos).right
                End If
            End If
        End While
    End Sub

    Sub showBT()
        Dim count As Integer
        For count = 1 To 10
            Console.WriteLine(BT(count).left & Space(5) & _
                              BT(count).data & Space(5) & BT(count).right)
        Next
    End Sub
End Module
