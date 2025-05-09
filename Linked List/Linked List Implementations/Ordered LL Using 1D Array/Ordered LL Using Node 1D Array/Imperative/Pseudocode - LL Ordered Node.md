```
CONSTANT NULL_POINTER ← -1

TYPE node 
    DECLARE data : CHARACTER 
    DECLARE next : INTEGER
END TYPE

DECLARE head, tail, free : INTEGER
DECLARE lst : ARRAY[0:9] OF node
```
```
PROCEDURE init_free_list()
    free ← 0
    head ← NULL_POINTER
    tail ← NULL_POINTER
    FOR i ← 0 TO 8
        lst[i].next ← i + 1
    NEXT i
    lst[9].next ← NULL_POINTER
ENDPROCEDURE
```
```
PROCEDURE add_list_item(item)
    IF free = NULL_POINTER THEN
        OUTPUT "List is full. Cannot add more items."
        EXIT PROCEDURE
    ENDIF

    IF head = NULL_POINTER THEN
        head ← free
        tail ← free
        free ← lst[free].next
        lst[head].data ← item
        lst[head].next ← NULL_POINTER
        EXIT PROCEDURE
    ENDIF

    IF item < lst[head].data THEN
        temp ← lst[free].next
        lst[free].data ← item
        lst[free].next ← head
        head ← free
        free ← temp
        EXIT PROCEDURE
    ENDIF

    IF item > lst[tail].data THEN
        temp ← lst[free].next
        lst[free].data ← item
        lst[free].next ← NULL_POINTER
        lst[tail].next ← free
        tail ← free
        free ← temp
        EXIT PROCEDURE
    ENDIF

    current ← head
    WHILE item > lst[lst[current].next].data
        current ← lst[current].next
    ENDWHILE

    temp ← lst[free].next
    lst[free].data ← item
    lst[free].next ← lst[current].next
    lst[current].next ← free
    free ← temp
ENDPROCEDURE
```
```
PROCEDURE print_list()
    current ← head
    WHILE current != NULL_POINTER
        OUTPUT lst[current].data
        current ← lst[current].next
    ENDWHILE
ENDPROCEDURE
```
```
FUNCTION search_list_item(item) RETURNS INTEGER
    current ← head
    WHILE current != NULL_POINTER
        IF lst[current].data = item THEN
            RETURN current
        ENDIF
        current ← lst[current].next
    ENDWHILE
    RETURN NULL_POINTER
ENDPROCEDURE
```
```
PROCEDURE print_array()
    OUTPUT "lst[] array:"
    OUTPUT "index  data  next"
    FOR i ← 0 TO 9
        OUTPUT i, lst[i].data, lst[i].next
    NEXT i
    OUTPUT "head = ", head
    OUTPUT "tail = ", tail
    OUTPUT "free = ", free
ENDPROCEDURE
```
```
PROCEDURE delete_list_item(item)
    GLOBAL head, tail, free

    IF head = NULL_POINTER THEN
        OUTPUT "List is empty"
        EXIT PROCEDURE
    ENDIF

    IF item = lst[head].data THEN
        temp ← head
        head ← lst[head].next
        lst[temp].next ← free
        free ← temp
        lst[free].data ← ''
        EXIT PROCEDURE
    ENDIF

    IF item = lst[tail].data THEN
        current ← head
        WHILE lst[current].next != tail
            current ← lst[current].next
        ENDWHILE
        lst[current].next ← NULL_POINTER
        lst[tail].next ← free
        free ← tail
        tail ← current
        lst[free].data ← ''
        EXIT PROCEDURE
    ENDIF

    current ← head
    WHILE item != lst[lst[current].next].data
        current ← lst[current].next
        IF lst[current].next = NULL_POINTER THEN
            OUTPUT "Item not found"
            EXIT PROCEDURE
        ENDIF
    ENDWHILE

    temp ← lst[current].next
    lst[current].next ← lst[lst[current].next].next
    lst[temp].next ← free
    free ← temp
    lst[free].data ← ''
ENDPROCEDURE
```
```
CALL init_free_list()
DECLARE option : INTEGER
option ← 0
WHILE option != 6
    OUTPUT "1. Add a node"
    OUTPUT "2. Delete a node"
    OUTPUT "3. Print the list"
    OUTPUT "4. Print the array"
    OUTPUT "5. Search an item"
    OUTPUT "6. Exit"
    INPUT option
    IF option = 1 THEN
        INPUT item
        CALL add_list_item(item)
    ELSE IF option = 2 THEN
        INPUT item
        CALL delete_list_item(item)
    ELSE IF option = 3 THEN
        CALL print_list()
    ELSE IF option = 4 THEN
        CALL print_array()
    ELSE IF option = 5 THEN
        INPUT item
        DECLARE index ← CALL search_list_item(item)
        IF index = NULL_POINTER THEN
            OUTPUT "Item not found."
        ELSE
            OUTPUT "Item found at index", index
        END IF
    ELSE IF option = 6 THEN
        OUTPUT "Goodbye!"
    ELSE
        OUTPUT "Invalid option"
    END IF
END WHILE
```