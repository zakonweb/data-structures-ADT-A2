import sys


def addQ(value):
    global EndOfQueuePointer, FrontOfQueuePointer, Queue, EmptyQ, UB, nullpointer, FullQ
    if FullQ:
        print("Overflow, data can't be deleted from the Queue.")
    else:
        if EndOfQueuePointer == UB and FrontOfQueuePointer > nullpointer:
            EndOfQueuePointer = LBound
        else:
            EndOfQueuePointer +=1
        Queue[EndOfQueuePointer] = value
        EmptyQ = False
        if EndOfQueuePointer == FrontOfQueuePointer or (EndOfQueuePointer == UB and FrontOfQueuePointer == nullpointer):
            FullQ = True
    return

def deleteQ():
    global EmptyQ, nullpointer, FrontOfQueuePointer, Queue, UB, LBound, FullQ, EndOfQueuePointer
    value = 0
    if EmptyQ:
        value = nullpointer
    else:
        if FrontOfQueuePointer == UB:
            FrontOfQueuePointer = LBound
        else:
            FrontOfQueuePointer +=1
        value = Queue[FrontOfQueuePointer]
        FullQ = False
        if FrontOfQueuePointer == EndOfQueuePointer:
            EmptyQ = True
        return value



UB = 5
LBound = 0
nullpointer = -1
FullQ = False
EmptyQ = True
Queue = []
for i in range(6):
    Queue.append(0)
FrontOfQueuePointer = nullpointer
EndOfQueuePointer = nullpointer
choice = 4

while choice != 3:
    choice = 0
    print("1. Add to Q\n2. Delete from Q\n3. Quit.")
    while not 1<=choice<=3:
        choice = int(input("Enter choice (1..3) "))
    if choice == 1:
        value = int(input("Enter value to add to Queue: "))
        addQ(value)
    elif choice == 2:
        value = deleteQ()
        if value == nullpointer:
            print("Underflow, Item can't be deleted from the Queue.")
        else:
            print("Item deleted =", value)