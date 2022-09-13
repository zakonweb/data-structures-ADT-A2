Module Module1
    Structure QNode
        Dim V As Char
        Dim P As Integer
    End Structure

    Dim QUEUE(5) As QNode
    Dim HP, TP, FP As Integer

    Sub Main()
        HP = 0
        TP = 0
        FP = 1

        Dim menuOp As Integer
        Dim d As Char

        Do
            Do
                Console.WriteLine("1. Add data to QUEUE.")
                Console.WriteLine("2. Remove data from QUEUE.")
                Console.WriteLine("3. Initialise QUEUE.")
                Console.WriteLine("4. Quit program.")
                menuOp = Console.ReadLine
            Loop Until menuOp >= 1 And menuOp <= 4

            Select Case menuOp
                Case 1
                    Console.Write("Enter Value to Add :") : d = Console.ReadLine
                    Call AddQ(d)
                Case 2
                    d = removeQ()
                    Console.WriteLine("VALUE REMOVED WAS : " & d)
                Case 3 : Call InitQ()
            End Select
        Loop Until menuOp = 4
    End Sub

    Sub AddQ(ByVal d As Char)
        If FP = 0 Then
            Console.WriteLine("OVERFLOW")
        Else
            HP = FP
            QUEUE(HP).V = d
            FP = QUEUE(HP).P
        End If
    End Sub

    Sub InitQ()
        Dim i As Integer = 0
        For i = 1 To 4
            QUEUE(i).V = ""
            QUEUE(i).P = i + 1
        Next

        QUEUE(5).P = 0
        HP = 0
        TP = 0
        FP = 1
    End Sub

    Function removeQ() As Char
        If HP = TP Then
            Console.WriteLine("UNDERFLOW")
            Return "0"
        Else
            TP += 1
            Return QUEUE(TP).V
        End If
    End Function
End Module