```
//SETUP BINARY TREE
RECORD bTreeNode
  DECLARE LeftPtr : INTEGER
  DECLARE Data : CHARACTER
  DECLARE RightPtr : INTEGER
END RECORD

DECLARE FreeNodePtr : INTEGER
DECLARE Tree : ARRAY [0:9] OF bTreeNode
```
```
PROCEDURE initialiseTree
  DECLARE i : INTEGER
  FreeNodePtr ← 0
  FOR i ← 0 TO 9
    Tree[i].LeftPtr ← -1
    Tree[i].Data ← ''
    Tree[i].RightPtr ← -1
  NEXT 
END PROCEDURE
```
```
PROCEDURE addNode(newItem : CHARACTER)
  DECLARE currNode : INTEGER
  DECLARE isAdded : BOOLEAN
  currNode ← 0 //Root Node
  isAdded ← False

  IF Tree[currNode].Data = ''
    THEN
      Tree[currNode].Data = newItem
      FreeNodePtr ← FreeNodePtr +1
    ELSEIF FreeNodePtr > 9
      THEN
        OUTPUT "Overflow occured.", newItem, "is not added."
    ELSE
      Tree[FreeNodePtr].Data = newItem
      WHILE isAdded = False
         IF newItem < Tree[currNode].Data
           THEN 
             IF Tree[currNode].LeftPtr = -1
               THEN
                 Tree[currNode].LeftPtr ← FreeNodePtr
	         isAdded = True
               ELSE
                 currNode ← Tree[currNode].LeftPtr
             ENDIF
         ELSE
           IF Tree[currPNode].RighPtr = -1
             THEN
               Tree[currNode].RightPtr ← FeeNodePtr
               isAdded = True
             ELSE
               currNode ← Tree[currNode].RightPtr
             END IF
         END IF
      END WHILE
      FreeNodePtr ← FreeNodePtr +1
  END IF
END PROCEDURE
```