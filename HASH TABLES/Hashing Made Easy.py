def InsertHash(RecKey):
    global studArr
    hashKey = Hash(RecKey, 10)
    while studArr[hashKey] != 0:
        hashKey +=1
        if hashKey>10:
            hashKey = 0
    studArr[hashKey] = RecKey
    return

def SearchHash(RecKey):
    global studArr
    totSearches = 0
    hashKey = Hash(RecKey, 10)
    while studArr[hashKey] != RecKey:
        totSearches +=1
        hashKey +=1
        if hashKey>10:
            hashKey = 0
        if totSearches>10:
            return 0
    return RecKey

def Hash(KeyVal, MaxPos):
    indexPos = KeyVal % (MaxPos+1)
    return indexPos


studArr = []
for i in range(11):
    studArr.append(0)

for x in range(11):
    RK = int(input("Enter Record Key: "))
    InsertHash(RK)
RK = int(input("Enter Search Record Key:"))
x = SearchHash(RK)
if x==0:
    print("Not Found")
else:
    print("Found")

for x in range(11):
    print(studArr[x])