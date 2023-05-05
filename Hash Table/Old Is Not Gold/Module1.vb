Module Module1
    Dim studArr(10) As Integer

    Sub Main()
        Dim RK, x As Integer
        For x = 0 To 10
            Console.Write("Enter Record Key :") : RK = Console.ReadLine
            Call InsertHash(RK)
        Next

        Console.Write("Enter Search Record Key :") : RK = Console.ReadLine
        x = SearchHash(RK)
        If x = 0 Then
            Console.WriteLine("Not Found")
        Else
            Console.WriteLine("Found")
        End If
        Console.ReadKey()

        For x = 0 To 10
            Console.WriteLine(studArr(x))
        Next
        Console.ReadKey()
    End Sub

    Sub InsertHash(ByVal RecKey As Integer)
        Dim hashKey As Integer
        hashKey = Hash(RecKey, 10)
        While studArr(hashKey) <> 0
            hashKey = hashKey + 1
            If hashKey > 10 Then hashKey = 0
        End While
        studArr(hashKey) = RecKey
    End Sub

    Function SearchHash(ByVal RecKey As Integer) As Integer
        Dim hashKey, totSearches As Integer
        hashKey = Hash(RecKey, 10)
        While studArr(hashKey) <> RecKey
            totSearches = totSearches + 1
            hashKey = hashKey + 1
            If hashKey > 10 Then hashKey = 0
            If totSearches > 10 Then
                Return 0
                Exit Function
            End If
        End While
        Return RecKey
    End Function

    Function Hash(ByVal KeyVal As Integer, ByVal MaxPos As Integer) As Integer
        Dim indexPos As Integer
        indexPos = Keyval Mod (MaxPos + 1)
        Return indexPos
    End Function
End Module
