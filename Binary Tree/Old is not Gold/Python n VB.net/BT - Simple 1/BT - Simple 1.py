BT = []


def Insert(val):
    global BT
    isInserted = False
    Pos = 0
    while not isInserted:
        if BT[Pos].left == 0 and BT[Pos].right == 0 and BT[Pos].data == "":
            isInserted = True
            BT[Pos].data = val
            break

        if val < BT[Pos].data != "":
            if BT[Pos].left == 0:
                N = Pos
                while BT[N].data != "":
                    N += 1
                if N > 10: return None
                BT[Pos].left = N
            else:
                Pos = BT[Pos].left

        if val > BT[Pos].data != "":
            if BT[Pos].right == 0:
                N = Pos
                while BT[N].data != "":
                    N += 1
                if N > 10: return None
                BT[Pos].right = N
            else:
                Pos = BT[Pos].right


def showBT():
    for count in range(10):
        print(BT[count].left, "   ", BT[count].data, "   ", BT[count].right)


class binaryTree:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


for i in range(10):
    BT.append(binaryTree("", 0, 0))
print("ONLY ENTER UNIQUE VALUES")
for i in range(10):
    myVal = input("Enter Val to Insert to BT :")
    Insert(myVal)

showBT()
