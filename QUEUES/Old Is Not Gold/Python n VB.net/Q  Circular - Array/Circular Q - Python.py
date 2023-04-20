# insert item, enqueue
def enQ(queue, item):
    global Qlen, Qfull, rearP, ub
    if Qlen < Qfull:
        if rearP < ub:
            rearP = rearP +1
        else:
            rearP = 0
        queue[rearP] = item
        Qlen = Qlen +1
    else:
        print("Overflow error, queue is full. Item cannot be added.")

# delete item, dequeue
def deQ(queue):
    global Qlen, frontP, ub
    if Qlen == 0:
        return -1
    else:
        item = queue[frontP]
        queue[frontP] = None
        if frontP == ub:
            frontP = 0
        else:
            frontP = frontP +1
        Qlen = Qlen -1
        return item

# Setting up the Queue
queue = [None for i in range(0,5)]
frontP = 0
rearP = -1
ub = 4
Qfull = 5
Qlen = 0

print(queue)
enQ(queue,27)
print(queue)
enQ(queue,34)
print(queue)
enQ(queue,93)
print(queue)
enQ(queue,20)
print(queue)

x = deQ(queue)
if x == -1:
    print ("Underflow error, queue is empty")
else:
    print(x, " is removed.")
    print(queue)

enQ(queue,31)
print(queue)
enQ(queue,55)
print(queue)
enQ(queue,65)
print(queue)

x = deQ(queue)
if x == -1:
    print ("Underflow error, queue is empty")
else:
    print(x, " is removed.")
    print(queue)

enQ(queue,75)
print(queue)