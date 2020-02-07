Module Module1
    Structure BT
        Dim LP As Integer
        Dim btData As String
        Dim RP As Integer
    End Structure

    Dim dsBT(10) As BT

    Sub Main()
        Dim Count As Integer
        Dim valBT As String
        Dim moreDE As Boolean = False
        For Count = 0 To 10
            dsBT(Count).LP = 0
            dsBT(Count).btData = ""
            dsBT(Count).RP = 0
        Next

        For Count = 0 To 10

            Console.Write("Enter Character :") : valBT = Console.ReadLine

            Call insertBT(valBT)
        Next

        For Count = 0 To 10
            Console.WriteLine(Count & Space(7) & dsBT(Count).LP & "    " & dsBT(Count).btData & "      " & dsBT(Count).RP)
        Next
        Console.ReadKey()
    End Sub

    Sub insertBT(ByVal val As String)
        Dim currPos As Integer = 0
        Dim tPos As Integer = 0
        While True
            If dsBT(currPos).btData = "" Then
                dsBT(currPos).btData = val
                Exit While
            ElseIf val > dsBT(currPos).btData Then
                If dsBT(currPos).RP = 0 Then
                    tPos = currPos
                    While dsBT(tPos).btData <> ""
                        tPos += 1
                    End While
                    dsBT(tPos).btData = val
                    dsBT(currPos).RP = tPos
                    Exit While
                Else
                    currPos = dsBT(currPos).RP
                End If
            Else
                If dsBT(currPos).LP = 0 Then
                    tPos = currPos
                    While dsBT(tPos).btData <> ""
                        tPos += 1
                    End While
                    dsBT(tPos).btData = val
                    dsBT(currPos).LP = tPos
                    Exit While
                Else
                    currPos = dsBT(currPos).LP
                End If

            End If
        End While
    End Sub
End Module
