```
//Setup a Stack ADT
DECLARE stack : ARRAY [0:9] OF INTEGER
DECLARE topPointer : INTEGER
DECLARE basePointer : INTEGER
DECLARE stackFull : INTEGER

basePointer ← 0
topPointer ← -1
stackFull ← 9
```
```
//Push an Item to stack
PROCEDURE push(item : INTEGER)
IF topPointer < stackFull
  THEN
    topPopinter ← topPointer +1
    stack[topPointer] ← item
  ELSE
    OUTPUT "Overflow occurs, cannot PUSH.)"
END IF
END PROCEDURE
```
```
//Pop an Item from Stack
FUNCTION pop() : INTEGER
IF topPointer = basePointer -1
  THEN
    OUTPUT "Underflow occurs, cannot POP.)"
    RETURN -1
  ELSE
    item ← stack[topPointer]
    topPointer ← topPointer -1
ENDIF
RETURN item
END FUNCTION
```