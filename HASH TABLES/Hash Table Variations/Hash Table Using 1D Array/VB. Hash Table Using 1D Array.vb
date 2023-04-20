Imports System

Module HashTableExample
    Sub Main()
        Dim hashTable(10) As Integer

        For i As Integer = 0 To 10
            Console.Write("Enter Record Key: ")
            Dim recordKey As Integer = Integer.Parse(Console.ReadLine())
            InsertHash(recordKey, hashTable)
        Next

        Console.Write("Enter Search Record Key: ")
        Dim searchRecordKey As Integer = Integer.Parse(Console.ReadLine())
        Dim foundIndex As Integer = SearchHash(searchRecordKey, hashTable)
        If foundIndex = -1 Then
            Console.WriteLine("Not Found")
        Else
            Console.WriteLine("Found")
        End If

        For Each item As Integer In hashTable
            Console.WriteLine(item)
        Next
    End Sub

    Sub InsertHash(ByVal recordKey As Integer, ByRef hashTable() As Integer)
        Dim index As Integer = HashFunction(recordKey, hashTable.Length - 1)
        While hashTable(index) <> 0
            index += 1
            If index > hashTable.Length - 1 Then
                index = 0
            End If
        End While
        hashTable(index) = recordKey
    End Sub

    Function SearchHash(ByVal recordKey As Integer, ByVal hashTable() As Integer) As Integer
        Dim totalSearches As Integer = 0
        Dim index As Integer = HashFunction(recordKey, hashTable.Length - 1)
        While hashTable(index) <> recordKey
            totalSearches += 1
            index += 1
            If index > hashTable.Length - 1 Then
                index = 0
            End If
            If totalSearches > hashTable.Length - 1 Then
                Return -1
            End If
        End While
        Return index
    End Function

    Function HashFunction(ByVal keyValue As Integer, ByVal maxPosition As Integer) As Integer
        Return keyValue Mod (maxPosition + 1)
    End Function
End Module
