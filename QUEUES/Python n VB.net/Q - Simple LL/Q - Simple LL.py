HP = TP = FP = 0
QUEUE = []


def initQ():
    global QUEUE, FP, TP, HP
    for i in range(5):
        QUEUE.append(QNode("", i + 1))
    QUEUE[4].p = 0
    HP = TP = 0
    FP = 1


def AddQ(d):
    global QUEUE, FP, TP, HP
    if FP == 0:
        print("OVERFLOW")
    else:
        HP = FP
        QUEUE[HP].v = d
        FP = QUEUE[HP].p


def removeQ():
    global QUEUE, FP, TP, HP
    if HP == TP:
        print("UNDERFLOW")
        return "0"
    else:
        TP += 1
        return QUEUE[TP].v


class QNode:
    def __init__(self, v, p):
        self.v = v
        self.p = p


menuOp = 0
while menuOp != 4:
    menuOp = 0
    while not 1 <= menuOp <= 4:
        print("1. Add data to QUEUE.\n2. Remove data from QUEUE.\n3. Initialise QUEUE.\n4. Quit program.")
        menuOp = int(input())

    if menuOp == 1:
        d = input("Enter Value to Add :")
        AddQ(d)
    elif menuOp == 2:
        d = removeQ()
        print("VALUE REMOVED WAS :", d)
    elif menuOp == 3:
        initQ()

