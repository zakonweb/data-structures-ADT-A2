Free = Temp = Temp2 = Current = ListStart = 0
List1 = []


def listInitialise():
    global List1
    for i in range(12):
        List1.append(LinkedList("", -1))


def ListDisplay():
    global List1
    for a in range(12):
        print(a, ".     ", List1[a].Data, ":", List1[a].Pointer)


def ListAdd():
    global Free, Temp, Temp2, Current, ListStart, List1
    d = input("Enter item to add.....")

    if Free == -1:
        print("Overflow")
    else:
        if Free == 0:
            List1[Free].Data = d
            ListStart = Free
            if List1[Free].Pointer == -1:
                Free += 1
            else:
                Free = List1[Free].Pointer
            if Free == 12: Free = -1
        else:
            if List1[ListStart].Data > d:
                List1[Free].Data = d
                List1[Free].Pointer = ListStart
                ListStart = Free
                if List1[Free].Pointer == -1:
                    Free += 1
                else:
                    Free = List1[Free].Pointer
                if Free == 12: Free = -1
            else:
                Current = ListStart
                while List1[List1[Current].Pointer].Data < d:
                    Current = List1[Current].Pointer
                    if List1[Current].Pointer == -1:
                        break
                List1[Free].Data = d

                Temp = List1[Current].Pointer
                List1[Current].Pointer = Free
                List1[Free].Pointer = Temp
                if List1[Free].Pointer == -1:
                    Free += 1
                else:
                    Free = List1[Free].Pointer
                if Free == 12: Free = -1


def listDelete():
    global Free, Temp, Temp2, Current, ListStart, List1
    d = input()
    if ListStart == -1:
        print("Underflow")
    else:
        isDeleted = False
        Current = ListStart
        while List1[List1[Current].Pointer].Data != d:
            Current = List1[Current].Pointer
            if List1[Current].Pointer == -1:
                break

        if List1[Current].Pointer != -1:
            Temp = List1[Current].Pointer
            List1[Current].Pointer = List1[List1[Current].Pointer].Pointer
            Temp2 = Free
            Free = Temp
            List1[Free].Pointer = Temp2
            isDeleted = True

        if not isDeleted:
            print("Data not deleted as it is not found.")


def ListSearch():
    d = input()

    Current = ListStart
    while List1[Current].Data != d or List1[Current].Pointer != -1:
        Current = List1[Current].Pointer

    if List1[Current].Data == d:
        print("Item Found.")
    else:
        print("Item Not Found.")


class LinkedList:
    def __init__(self, Data, Pointer):
        self.Data = Data
        self.Pointer = Pointer


MenuOption = 1
listInitialise()
while not MenuOption == 0:
    print("1. Add item to list.\n2. Delete item from list.\n3. Display items in list.\n4. Search item in List.\n0. Quit.\n")
    MenuOption = int(input("Enter your choice....."))
    if MenuOption == 1:
        ListAdd()
    elif MenuOption == 2:
        listDelete()
    elif MenuOption == 3:
        ListDisplay()
    elif MenuOption == 4:
        ListSearch()
