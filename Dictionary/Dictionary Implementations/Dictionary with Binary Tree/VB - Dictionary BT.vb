Public Class Node
    Public key As Integer
    Public value As String
    Public left As Node = Nothing
    Public right As Node = Nothing
    Public Sub New(ByVal item As Integer, ByVal value As String)
        key = item
        Me.value = value
    End Sub
End Class

Public Class BinaryTree
    Public root As Node = Nothing
    Public Sub insert(ByVal key As Integer, ByVal value As String)
        root = insertRec(root, key, value)
    End Sub

    Private Function insertRec(ByVal root As Node, ByVal key As Integer, ByVal value As String) As Node
        If root Is Nothing Then
            root = New Node(key, value)
            Return root
        End If
        If key < root.key Then
            root.left = insertRec(root.left, key, value)
        ElseIf key > root.key Then
            root.right = insertRec(root.right, key, value)
        Else
            root.value = value ' If the key already exists, update the value
        End If
        Return root
    End Function

    Public Function search(ByVal key As Integer) As Node
        Return searchRec(root, key)
    End Function

    Private Function searchRec(ByVal root As Node, ByVal key As Integer) As Node
        If root Is Nothing OrElse root.key = key Then
            Return root
        End If
        If root.key > key Then
            Return searchRec(root.left, key)
        End If
        Return searchRec(root.right, key)
    End Function
End Class
