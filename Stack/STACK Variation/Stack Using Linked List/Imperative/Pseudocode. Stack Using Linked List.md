```
TYPE Node
    data : INTEGER
    pointer : INTEGER
END TYPE

CONSTANT MAX ← 10
CONSTANT NULL_POINTER ← -1

//GLOBAL VARIABLES
DECLARE topOfStack : INTEGER
DECLARE head : INTEGER
DECLARE free : INTEGER
DECLARE stack : ARRAY[0 TO MAX-1] OF Node
```
```
PROCEDURE Main()
    CALL InitializeStack()

    DECLARE data : INTEGER
    DECLARE Choice : INTEGER ← 0

    WHILE Choice <> 5
        OUTPUT "Stack Using Linked List"
        OUTPUT "1. Push"
        OUTPUT "2. Pop"
        OUTPUT "3. Display Stack"
        OUTPUT "4. Print Linked List Array"
        OUTPUT "5. Exit"
        OUTPUT "Enter your choice: "
        INPUT Choice

        CASE Choice OF
            1: 
                OUTPUT "Enter integer data: "
                INPUT data
                CALL Push(data)
            2: 
                DECLARE poppedData : INTEGER?
                poppedData ← Pop()
                IF poppedData <> NULL THEN
                    OUTPUT "Popped element: " & poppedData
                ENDIF
            3:
                CALL DisplayStack()
            4:
                CALL DisplayArray()
            5:
                OUTPUT "Thank You"
            ELSE
                OUTPUT "Invalid Choice"
        END CASE
    END WHILE
END PROCEDURE
```
```
PROCEDURE InitializeStack()
    topOfStack ← NULL_POINTER
    head ← NULL_POINTER
    free ← 0

    FOR i ← 0 TO MAX - 2
        stack[i].data = 0
        stack[i].pointer ← i + 1
    NEXT i

    stack[MAX - 1].pointer ← NULL_POINTER
END PROCEDURE
```
```
PROCEDURE Push(data : INTEGER)
    DECLARE temp : INTEGER 
    temp ← free

    IF free = NULL_POINTER THEN
        OUTPUT "Stack Overflow"
    ELSE
        free ← stack[free].pointer
        stack[temp].data ← data
        stack[temp].pointer ← topOfStack
        topOfStack ← temp

        IF head = NULL_POINTER THEN
            head ← topOfStack
        ENDIF
    ENDIF
END PROCEDURE
```
```
FUNCTION Pop() RETURNS INTEGER
    DECLARE val : INTEGER
    DECLARE temp : INTEGER 
    temp ← topOfStack

    IF topOfStack = NULL_POINTER THEN
        OUTPUT "Stack Underflow"
        RETURN -1
    ELSE
        topOfStack ← stack[topOfStack].pointer
        stack[temp].pointer ← free
        free ← temp

        IF topOfStack = NULL_POINTER THEN
            head ← NULL_POINTER
        ENDIF

        val ← stack[temp].data
        stack[temp].data ← 0
        RETURN val
    ENDIF
END FUNCTION
```
```
PROCEDURE DisplayStack()
    DECLARE temp : INTEGER 
    temp ← topOfStack

    IF topOfStack = NULL_POINTER THEN
        OUTPUT "Stack is Empty"
    ELSE
        WHILE temp <> NULL_POINTER
            IF temp = topOfStack THEN
                OUTPUT stack[temp].data & " <---"
            ELSE
                OUTPUT stack[temp].data
            ENDIF
            temp ← stack[temp].pointer
        END WHILE
    ENDIF
END PROCEDURE
```
```
PROCEDURE DisplayArray()
    OUTPUT "index" & " data" & " next"
    FOR i ← 0 TO MAX - 1
        OUTPUT i & " " & stack[i].data & " " & stack[i].pointer

        IF i = free THEN
            OUTPUT " free"
        ELSIF i = topOfStack THEN
            OUTPUT " top_of_stack | tail_of_LL"
        ELSIF i = head THEN
            OUTPUT " head"
    	ELSE
            OUTPUT ""
        ENDIF
    NEXT i
    OUTPUT "top_of_stack: " & topOfStack
    OUTPUT "head: " & head
    OUTPUT "free: " & free
END PROCEDURE
```