```
CONSTANT NULL_POINTER ← -1

DECLARE head, tail, free : INTEGER
DECLARE data : ARRAY[0:9] OF CHARACTER
DECLARE next : ARRAY[0:9] OF INTEGER
```
```
PROCEDURE init_free_list()
    free ← 0
    head ← NULL_POINTER
    tail ← NULL_POINTER
    FOR i ← 0 TO 8
        next[i] ← i + 1
    NEXT i
    next[9] ← NULL_POINTER
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
        free ← next[free]
        data[head] ← item
        next[head] ← NULL_POINTER
        EXIT PROCEDURE
    ENDIF

    IF item < data[head] THEN
        temp ← next[free]
        data[free] ← item
        next[free] ← head
        head ← free
        free ← temp
        EXIT PROCEDURE
    ENDIF

    IF item > data[tail] THEN
        temp ← next[free]
        data[free] ← item
        next[free] ← NULL_POINTER
        next[tail] ← free
        tail ← free
        free ← temp
        EXIT PROCEDURE
    ENDIF

    current ← head
    WHILE item > data[next[current]]
        current ← next[current]
    ENDWHILE

    temp ← next[free]
    data[free] ← item
    next[free] ← next[current]
    next[current] ← free
    free ← temp
ENDPROCEDURE

```
```
PROCEDURE print_list()
    current ← head
    WHILE current != NULL_POINTER
        OUTPUT data[current]
        current ← next[current]
    ENDWHILE
ENDPROCEDURE
```
```
FUNCTION search_list_item(item) RETURNS INTEGER
    current ← head
    WHILE current != NULL_POINTER
        IF data[current] = item THEN
            RETURN current
        ENDIF
        current ← next[current]
    ENDWHILE
    RETURN NULL_POINTER
ENDFUNCTION
```
```
PROCEDURE print_array()
    OUTPUT "Array:"
    OUTPUT "index  data  next"
    FOR i ← 0 TO 9
        OUTPUT i, data[i], next[i]
    NEXT i
    OUTPUT "head = ", head
    OUTPUT "tail = ", tail
    OUTPUT "free = ", free
ENDPROCEDURE
```
```
PROCEDURE delete_list_item(item)
    IF head = NULL_POINTER THEN
        OUTPUT "List is empty"
        EXIT PROCEDURE
    ENDIF

    IF item = data[head] THEN
        temp ← head
        head ← next[head]
        next[temp] ← free
        free ← temp
        data[free] ← ''
        EXIT PROCEDURE
    ENDIF

    IF item = data[tail] THEN
        current ← head
        WHILE next[current] != tail
            current ← next[current]
        ENDWHILE
        next[current] ← NULL_POINTER
        next[tail] ← free
        free ← tail
        tail ← current
        data[free] ← ''
        EXIT PROCEDURE
    ENDIF

    current ← head
    WHILE item != data[next[current]]
        current ← next[current]
        IF next[current] = NULL_POINTER THEN
            OUTPUT "Item not found"
            EXIT PROCEDURE
        ENDIF
    ENDWHILE

    temp ← next[current]
    next[current] ← next[next[current]]
    next[temp] ← free
    free ← temp
    data[free] ← ''
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