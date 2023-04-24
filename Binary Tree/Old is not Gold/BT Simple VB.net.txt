 Module BinaryTreeInsert

    'Binary Tree ADT
    Structure BT
        Dim LeftPointer As Integer
        Dim Data As String
        Dim RightPointer As Integer
    End Structure

    'Array based on Binary Tree ADT
    Dim dsBT(10) As BT

    Sub Main()
        Dim Count As Integer
        Dim valBT As String
        Dim moreDE As Boolean = False

        'Initialise whole array. LP/RP to Null 0, Data to Null ""
        For Count = 0 To 10
            dsBT(Count).LeftPointer = 0
            dsBT(Count).Data = ""
            dsBT(Count).RightPointer = 0
        Next

        'Input game name and call insert function
        For Count = 0 To 9
            Console.Write("Enter Video Game Name " & Count + 1 & ": ") : valBT = Console.ReadLine
            Call insertBT(valBT)
        Next

        'Display binary tree after insertion
        For Count = 0 To 9
            Console.WriteLine(Count & Space(7) & dsBT(Count).LeftPointer & "    " & _
                              dsBT(Count).Data & Space(27 - Len(dsBT(Count).Data)) & dsBT(Count).RightPointer)
        Next

        Console.ReadKey()
    End Sub


    Sub insertBT(ByVal val As String)
        Dim currPos As Integer = 0
        Dim tPos As Integer = 0
        While True
            If dsBT(currPos).Data = "" Then
                dsBT(currPos).Data = val
                Exit While
            ElseIf val > dsBT(currPos).Data Then
                If dsBT(currPos).RightPointer = 0 Then
                    tPos = currPos
                    While dsBT(tPos).Data <> ""
                        tPos += 1
                    End While
                    dsBT(tPos).Data = val
                    dsBT(currPos).RightPointer = tPos
                    Exit While
                Else
                    currPos = dsBT(currPos).RightPointer
                End If
            Else
                If dsBT(currPos).LeftPointer = 0 Then
                    tPos = currPos
                    While dsBT(tPos).Data <> ""
                        tPos += 1
                    End While
                    dsBT(tPos).Data = val
                    dsBT(currPos).LeftPointer = tPos
                    Exit While
                Else
                    currPos = dsBT(currPos).LeftPointer
                End If
            End If
        End While
    End Sub
End Module
