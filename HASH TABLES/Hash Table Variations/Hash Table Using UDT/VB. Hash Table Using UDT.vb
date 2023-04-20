Structure Record
    Dim key As Integer
    Dim value As String
End Structure

Module Module1

    Sub Main()
	' Define variables to store record key, record value, 
	' record object, search key and found index
	Dim recordKey As Integer
	Dim recordValue As String
	Dim record As Record
	Dim searchRecordKey As Integer
	Dim foundIndex As Integer

	' Loop 11 times to get 11 record keys from the user and 
	' insert them into the hash table
	For i As Integer = 0 To 10
	    ' Prompt the user to enter a record key and read the input as an integer
	    Console.Write("Enter record key: ")
	    recordKey = Integer.Parse(Console.ReadLine())

	    ' Create a string for the record value using the record key
	    recordValue = $"Customer {recordKey}"

	    ' Create a new record object with the key and value
	    record = New Record With {.key = recordKey, .value = recordValue}

	    ' Call the InsertHash function to insert the record into the hash table
	    InsertHash(record, hashTable)
	Next

	' Prompt the user to enter a search key and read the input as an integer
	Console.Write("Enter Search Record Key: ")
	searchRecordKey = Integer.Parse(Console.ReadLine())

	' Call the SearchHash function to find the record with the given 
	' search key in the hash table
	foundIndex = SearchHash(searchRecordKey, hashTable)

	' Print the result of the search
	If foundIndex = -1 Then
	    Console.WriteLine("Not Found")
	Else
	    Console.WriteLine($"Found: {hashTable(foundIndex).value}")
	End If

	' Print the values of all the records in the hash table
	For Each item In hashTable
	    Console.WriteLine(item?.value)
	Next

	' Wait for user input before exiting the program
	Console.ReadLine()
    End Sub

    Function HashFunction(ByVal key As Integer, ByVal size As Integer) As Integer
        Return key Mod (size + 1)
    End Function

    Sub InsertHash(ByVal record As Record, ByVal hashTable() As Record)
        Dim index As Integer 
        index = HashFunction(record.key, hashTable.Length - 1)

        While Not hashTable(index) Is Nothing
            index += 1
            If index > hashTable.Length - 1 Then
                index = 0
            End If
        End While
        hashTable(index) = record
    End Sub

    Public Function SearchHash(ByVal recordKey As Integer, ByVal hashTable() As Record) As Integer
        Dim totSearches As Integer = 0
        Dim index As Integer 
        index = HashFunction(recordKey, hashTable.Length - 1)

        While Not hashTable(index) Is Nothing AndAlso hashTable(index).key <> recordKey
            totSearches += 1
            index += 1

            If index > hashTable.Length - 1 Then
                index = 0
            End If

            If totSearches > hashTable.Length - 1 Then
                Return -1
            End If
        End While

        If Not hashTable(index) Is Nothing Then
            Return index
        Else
            Return -1
        End If
    End Function

End Module
