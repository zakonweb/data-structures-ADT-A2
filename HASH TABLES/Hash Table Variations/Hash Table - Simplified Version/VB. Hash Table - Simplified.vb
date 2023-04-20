Imports System

Module SimpleHashTable
    Sub Main()
        ' Create an array to represent the hash table.
        Dim hashTable(9) As Integer?

        ' Insert some keys into the hash table.
        Dim keys() As Integer = {45876, 32390, 95312, 64636, 23467}
        For Each key As Integer In keys
            Insert(hashTable, key)
        Next

        ' Search for a key in the hash table.
        Console.Write("Enter a key to search: ")
        Dim searchKey As Integer = Integer.Parse(Console.ReadLine())
        Dim foundIndex As Integer = Search(hashTable, searchKey)
        If foundIndex = -1 Then
            Console.WriteLine("Key not found.")
        Else
            Console.WriteLine("Key found at index {0}", foundIndex)
        End If

        ' Print the hash table.
        For i As Integer = 0 To hashTable.Length - 1
            Console.Write("{0} ", hashTable(i))
        Next
    End Sub

    ' Define a function to calculate the index for a given key.
    Function HashFunction(ByVal key As Integer, ByVal tableSize As Integer) As Integer
        Return key Mod tableSize
    End Function

    ' Define a function to insert a key into the hash table.
    Sub Insert(ByRef hashTable() As Integer?, ByVal key As Integer)
        Dim index As Integer = HashFunction(key, hashTable.Length)
        While hashTable(index).HasValue
            index = (index + 1) Mod hashTable.Length
        End While
        hashTable(index) = key
    End Sub

    ' Define a function to search for a key in the hash table.
    Function Search(ByVal hashTable() As Integer?, ByVal key As Integer) As Integer
        Dim index As Integer = HashFunction(key, hashTable.Length)
        While hashTable(index).HasValue AndAlso hashTable(index) <> key
            index = (index + 1) Mod hashTable.Length
        End While
        Return If(hashTable(index).HasValue, index, -1)
    End Function
End Module
