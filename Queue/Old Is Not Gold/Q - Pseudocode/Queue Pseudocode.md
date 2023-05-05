```
//Queue ADT
//Circular Q.

//Setting up a Q
DECLARE Q : ARRAY [0:4] AS INTEGER
DECLARE UB, Qfull, Qlen, rearP, frontP : INTEGER

UB ← 4
Qfull ← 5 //Q is from element 0 to 4 = 5
Qlen ← 0
rearP ← -1
frontP ← 0

FOR i ← 0 TO 4
    Q[i] ← NONE
NEXT i
```
```
// INSERT AN ITEM, Enqueue
PROCEDURE EnQ(arr[], item : INTEGER)
  IF Qlen < Qfull
    THEN
      IF rearP < UB
        THEN
          rearP ← rearP +1
        ELSE
          rearP ← 0
      END IF
      
      Q[rearP] ← item
      Qlen ← Qlen +1
    ELSE
      OUTPUT "Overflow error, item cannot be added."
  END IF
END PROCEDURE
```
```
// DELETE AN ITEM, DEQUEUE
FUNCTION DeQ(arr[]) : INETEGER
  DECLARE item : INTEGER
  IF Qlen > 0
    THEN
      item ← Q[frontP]
      Q[frontP] ← NONE

      IF frontP = UB
        THEN
          frontP ← 0
        ELSE
          frontP ← frontP +1
      END IF
      Qlen ← Qlen -1

      RETURN item
    ELSE
      RETURN -1
  END IF
END FUNCTION
```