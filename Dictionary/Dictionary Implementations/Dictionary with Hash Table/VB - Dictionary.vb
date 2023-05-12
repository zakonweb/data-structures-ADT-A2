Imports System.Collections

Module Dictionary
    Dim ht As New Hashtable()

    Sub Main()
        Dim choice As Integer
        Do
            Console.WriteLine(vbCrLf & "1. Insert" & vbCrLf & "2. Delete" & vbCrLf & "3. Search" & vbCrLf & "4. Display" & vbCrLf & "5. Exit")
            Console.Write("Enter your choice: ")
            choice = Console.ReadLine()
            Select Case choice
                Case 1
                    Console.Write("Enter key: ")
                    Dim key As String = Console.ReadLine()
                    Console.Write("Enter value: ")
                    Dim value As String = Console.ReadLine()
                    ht.Add(key, value)
                Case 2
                    Console.Write("Enter key: ")
                    Dim key As String = Console.ReadLine()
                    If ht.ContainsKey(key) Then
                        ht.Remove(key)
                    Else
                        Console.WriteLine("Key not found!")
                    End If
                Case 3
                    Console.Write("Enter key: ")
                    Dim key As String = Console.ReadLine()
                    If ht.ContainsKey(key) Then
                        Console.WriteLine("Value: " & ht(key))
                    Else
                        Console.WriteLine("Key not found!")
                    End If
                Case 4
                    For Each key In ht.Keys
                        Console.WriteLine("{0} : {1}", key, ht(key))
                    Next
                Case 5
                    Exit Do
                Case Else
                    Console.WriteLine("Invalid choice!")
            End Select
        Loop While choice <> 5
    End Sub

End Module
