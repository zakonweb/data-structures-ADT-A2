//QUEUE ADT (Adjusting Queues)

DECLARE FrontPtr, RearPtr, UB : INTEGER
DECLARE Queue : ARRAY [1:10] OF CHARACTER

PROCEDURE initialseQ()
  DECLARE i : INTEGER

  FrontPtr ← 0
  RearPtr ← 0
  UB ← 10

  FOR i ← 1 TO 10
    Queue[i] = ''
  NEXT
END PROCEDURE

PROCEDURE Enqueue(data : CHARACTER)
  IF RearPtr = UB
    THEN
      OUTPUT "Error, Overflow occured."
    ELSE
      RearPtr  ← RearPtr +1
      Queue[RearPtr] = data
  END IF
END PROCEDURE

PROCEDURE Dequeue()
  IF RearPtr = 0
    THEN
      OUTPUT "Error, Underflow occured."
    ELSE
      FrontPtr ← FrontPtr +1
      OUTPUT Queue[FrontPtr]

      For i ← 1 TO UB -1
         Queue[i] ← Queue[i +1]
      Next 

      FrontPtr ← FrontPtr -1
      RearPtr ← RearPtr -1
  END IF
END PROCEDURE
