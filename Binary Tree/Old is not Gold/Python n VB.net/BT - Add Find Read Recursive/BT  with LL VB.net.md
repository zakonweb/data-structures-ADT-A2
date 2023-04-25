Module mBianryTree1
    ' NullPointer should be set to -1 if using array element with index 0
    Const NULLPOINTER = -1

    ' Declare record type to store data and pointer
    Structure TreeNode
        Dim LeftPointer As Integer
        Dim Data As String
        Dim RightPointer As Integer
    End Structure

    Const UB = 9
    Const LB = 0

    Dim Tree(UB) As TreeNode
    Dim RootPointer As Integer
    Dim FreePtr As Integer

    Sub Main()
        Dim Choice As Integer = 0
        Dim Data As String = ""
        Dim CurrentPtr As Integer = 0

        InitialiseTree()

        Do While Choice <> "4"
            Choice = GetOption()
            Select Case Choice
                Case "1"
                    Console.Write("Enter new data item... ")
                    Data = Console.ReadLine()
                    InsertNode(Data)

                Case "2"
                    Console.Write("Enter search value: ")
                    Data = Console.ReadLine()
                    CurrentPtr = FindNode(Data)
                    If CurrentPtr = NULLPOINTER Then
                        Console.WriteLine("Value not found")
                    Else
                        Console.WriteLine("value found at: " & CurrentPtr)
                    End If
                    Console.ReadKey()

                Case "3"
                    Console.WriteLine("Inorder Traversed Data")
                    Console.WriteLine("----------------------")
                    InOrderTraverse(RootPointer)

                    Console.WriteLine()
                    Console.WriteLine("Root Pointer = " & RootPointer & ", Free Pointer = " & FreePtr)
                    Console.WriteLine()
                    Console.WriteLine("Index " & "LP   " & "Data" & Space(26) & "RP")
                    For i = LB To UB
                        Console.WriteLine(i & Space(5) & Tree(i).LeftPointer & Space(5 - Len(Tree(i).LeftPointer.ToString)) & _
                                          Tree(i).Data & Space(30 - Len(Tree(i).Data)) & Tree(i).RightPointer)
                    Next
                    Console.ReadKey()
            End Select
        Loop
    End Sub

    Function GetOption() As Integer
        Dim Choice As Integer
        Console.Clear()
        Console.WriteLine("Binary Tree Main Menu")
        Console.WriteLine("1: Add Game")
        Console.WriteLine("2: Find Game")
        Console.WriteLine("3: Read/Traverse Binary Tree Inorder (left-root-right)")
        Console.WriteLine("4: Quit")
        Console.Write("Enter your choice: ")
        Choice = Val(Console.ReadLine())
        Return Choice
    End Function

    Sub InitialiseTree()
        RootPointer = NULLPOINTER ' set start pointer
        FreePtr = 0 ' set starting position of free list
        For Index = LB To UB 'link all nodes to make free list
            Tree(Index).LeftPointer = NULLPOINTER
            Tree(Index).Data = ""
            Tree(Index).RightPointer = Index + 1
        Next
        Tree(UB).RightPointer = NULLPOINTER 'last node of free list
    End Sub

    Function FindNode(ByVal SearchItem) As Integer
        Dim CurrentPtr As Integer
        CurrentPtr = RootPointer
        Try
            Do While CurrentPtr <> NULLPOINTER And Tree(CurrentPtr).Data <> SearchItem
                If Tree(CurrentPtr).Data > SearchItem Then
                    CurrentPtr = Tree(CurrentPtr).LeftPointer
                Else
                    CurrentPtr = Tree(CurrentPtr).RightPointer
                End If
            Loop
        Catch ex As Exception
        End Try
        Return CurrentPtr
    End Function

    Sub InsertNode(ByVal NewItem)
        Dim NewNodePtr, CurrentPtr, PrevNodePtr As Integer
        Dim TurnedLeft As Boolean

        If FreePtr <> NULLPOINTER Then
            ' there is space in the array
            ' take node from free list and store data item
            NewNodePtr = FreePtr
            Tree(NewNodePtr).Data = NewItem
            FreePtr = Tree(FreePtr).RightPointer
            Tree(NewNodePtr).RightPointer = NULLPOINTER

            ' check if empty tree
            If RootPointer = NULLPOINTER Then
                RootPointer = NewNodePtr

            Else ' find insertion point
                CurrentPtr = RootPointer
                Do While CurrentPtr <> NULLPOINTER
                    PrevNodePtr = CurrentPtr

                    If NewItem < Tree(CurrentPtr).Data Then
                        TurnedLeft = True
                        CurrentPtr = Tree(CurrentPtr).LeftPointer
                    Else
                        TurnedLeft = False
                        CurrentPtr = Tree(CurrentPtr).RightPointer
                    End If
                Loop

                If TurnedLeft = True Then
                    Tree(PrevNodePtr).LeftPointer = NewNodePtr
                Else
                    Tree(PrevNodePtr).RightPointer = NewNodePtr
                End If

            End If
        Else
            Console.WriteLine("Overflow occured. No space for more data...")
            Console.ReadKey()
        End If
    End Sub

    'Recursive function for INORDER Tree Traversal
    Sub InOrderTraverse(ByVal Root As Integer)
        If Root <> NULLPOINTER Then
            'Move Left , traverse left sub tree
            InOrderTraverse(Tree(Root).LeftPointer)

            'Output 
            Console.WriteLine(Tree(Root).Data)

            'Move Right, traverse right sub tree
            InOrderTraverse(Tree(Root).RightPointer)

        End If
    End Sub

End Module