//QUEUE ADT (Circular Queues)

DECLARE FrontPtr, RearPtr, Qsize, Qfull, UB : INTEGER
DECLARE Queue : ARRAY [1:10] OF CHARACTER

PROCEDURE initialseQ()
  DECLARE i : INTEGER

  FrontPtr ← 0
  RearPtr ← 0
  Qsize ← 0
  Qfull ← 10
  UB ← 10

  FOR i ← 1 TO 10
    Queue[i] = ''
  NEXT
END PROCEDURE

PROCEDURE Enqueue(data : CHARACTER)
  IF Qsize = Qfull
    THEN
      OUTPUT "Error, Overflow occured."
    ELSE
      IF RearPtr = UB
        THEN
          RearPtr ← 1
        ELSE
          RearPtr  ← RearPtr +1
      END IF
      Queue[RearPtr] = data
      Qsize ← Qsize +1
  END IF
END PROCEDURE

PROCEDURE Dequeue()
IF Qsize = 0
    THEN
      OUTPUT "Error, Underflow occured."
    ELSE
      IF FrontPtr = UB
        THEN
          FrontPtr ← 1
        ELSE
          FrontPtr ← FrontPtr +1
      END IF
      OUTPUT Queue[FrontPtr]
      Qsize ← Qsize -1
  END IF
END PROCEDURE
