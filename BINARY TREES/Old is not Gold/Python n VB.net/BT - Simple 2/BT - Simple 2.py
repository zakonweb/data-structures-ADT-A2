dsBT = []
Count = valBT = 0


def insertBT(val):
    currPos = 0
    tPos = 0
    while True:
        if dsBT[currPos].btData == "":
            dsBT[currPos].btData = val
            break
        elif val > dsBT[currPos].btData:
            if dsBT[currPos].RP == 0:
                tPos = currPos
                while dsBT[tPos].btData != "":
                    tPos += 1
                dsBT[tPos].btData = val
                dsBT[currPos].RP = tPos
                break
            else:
                currPos = dsBT[currPos].RP
        else:
            if dsBT[currPos].LP == 0:
                tPos = currPos
                while dsBT[tPos].btData != "":
                    tPos += 1
                dsBT[tPos].btData = val
                dsBT[currPos].LP = tPos
            else:
                currPos = dsBT[currPos].LP


class BT:
    def __init__(self, LP, btData, RP):
        self.LP = LP
        self.btData = btData
        self.RP = RP


for count in range(11):
    dsBT.append(BT(0, "", 0))

for count in range(11):
    valBT = input("Enter Character :")
    insertBT(valBT)

for count in range(11):
    print(Count, "     ", dsBT[Count].LP, "  ", dsBT[Count].btData, "    ", dsBT[Count].RP)
