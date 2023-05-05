```
DECLARE queue[9] : INTEGER
DECLARE front : INTEGER
DECLARE rear : INTEGER
DECLARE choice, data : INTEGER

front ← -1
rear ← -1
choice ← 0

WHILE TRUE
    OUTPUT "Enter 1 to enqueue an element"
    OUTPUT "Enter 2 to dequeue an element"
    OUTPUT "Enter 3 to display the queue"
    OUTPUT "Enter 4 to exit"
    OUTPUT "Enter your choice: "
    INPUT choice
    CASE OF choice
        1:
            OUTPUT "Enter the element to be enqueued: "
            INPUT data
            Enqueue(data)
        2:
            data ← Dequeue()
            IF data <> -1 THEN
                OUTPUT "The dequeued element is: " & data
            ENDIF
        3:
            CALL Display()
        4:
            EXIT WHILE
        OTHERWISE": OUTPUT "Invalid choice"
    END CASE
END WHILE
```
```
PROCEDURE Enqueue(data : INTEGER)
    ' Check if queue is full by checking if the rear pointer is one
    IF (rear + 1) MOD LENGTH[queue] = front THEN
        OUTPUT "Queue is full"
    ' If queue is empty, set front and rear pointers to 0
    ELSEIF front = -1 AND rear = -1 THEN
        front ← 0
        rear ← 0
        queue[rear] ← data
    ' If queue is not empty, move the rear pointer to the 
    ' next element and add the data to it
    ELSE
        rear ← (rear + 1) MOD LENGTH[queue]
        queue[rear] ← data
    ENDIF
END PROCEDURE
```
```
FUNCTION Dequeue() RETURNS INTEGER
    DECLARE data : INTEGER
    ' Check if queue is empty
    IF front = -1 AND rear = -1 THEN
        OUTPUT "Queue is empty"
        RETURN -1
    ' If queue has only one element, reset front and rear pointers
    ELSEIF front = rear THEN
        data ← queue[front]
        queue[front] ← -1
        front ← -1
        rear ← -1
        RETURN data
    ' If queue has more than one element, move the front pointer 
    ' to the next element and remove the data from it
    ELSE
        data ← queue[front]
        queue[front] ← -1
        front ← (front + 1) MOD LENGTH[queue]
        RETURN data
    ENDIF
END FUNCTION
```
```
PROCEDURE Display()
    DECLARE i : INTEGER
    ' Check if queue is empty
    IF front = -1 AND rear = -1 THEN
        OUTPUT "Queue is empty"
    ELSE
        OUTPUT "Elements in the queue: "
        ' Iterate through the elements in the queue and 
        ' print them out in order
        i ← front
        WHILE i <> rear
            OUTPUT queue[i] & " "
            i ← (i + 1) MOD LENGTH[queue]
        END WHILE
        OUTPUT queue[rear] & " "
        OUTPUT ""
        OUTPUT "Front: " & front
        OUTPUT "Rear: " & rear
        ' Print the size of the queue by subtracting the front
        ' pointer from the rear pointer and adding 1
        ' but if there is a wrap around at the end of the queue,
        ' then the size is calculated by subtracting the front
        ' pointer from the length of the queue and adding the
        ' rear pointer and adding 1
        IF front <= rear THEN
            OUTPUT "Size: " & (rear - front + 1)
        ELSE
            OUTPUT "Size: " & (LENGTH[queue] - front + rear + 1)
        ENDIF
    ENDIF
END PROCEDURE
```