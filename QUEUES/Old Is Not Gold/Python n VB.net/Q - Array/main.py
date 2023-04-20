import sys


def cmdPop_Click(): #This command is used to retrieve data from the queue
    global startptr, endptr, queue
    if startptr == endptr: #Checks if End pointer and Start pointer are in same location in which case the queue will be empty
        print("Underflow") #Displays Error message, stating that queue is empty
        return #Exits the private sub if error is detected
    print(queue[endptr]) #Retrieves value from queue and displays it
    endptr +=1 #Moves End Pointer to the next value stored in the queue
    return

def cmdPush_Click(): #This command is used to enter data into the queue
    global startptr, queue
    newVal = input("Enter New Value: ")#Declares and inputs a variable that is to be input into the queue
    if startptr > 9: #Checks if there is space in the queue for more data
        print("Overflow") #Displays error message, stating the queue is full
        return #Exits the private sub if error is detected
    queue[startptr] = newVal #Stores the value that was input into the queue
    startptr +=1 #Moves Start POinter to the next available space in the queue

def cmdReset_Click(): #This command is used to reset the queue and to make space available again
    global startptr, endptr
    startptr = 0 #Initializes the Start Pointer back to its original position
    endptr = 0 #Initialized the End Pointer back to its original position

queue = [] #declaring a list
for i in range(10): #initialising queue
    queue.append("")
startptr = 0 #declare and initialise virtual start pointer
endptr = 0 #declare and initialise virtual end pointer
menuchoice = 0
while menuchoice != 4:
    menuchoice = int(input("1. To PUSH to QUEUE\n2. To POP from QUEUE\n3. To RESET the QUEUE.\n4. To exit this module.\n"))
    if menuchoice == 1:
        cmdPush_Click()
    elif menuchoice == 2:
        cmdPop_Click()
    elif menuchoice == 3:
        cmdReset_Click()
    elif menuchoice == 4:
        sys.exit
    else:
        print("Wrong choice. Please try again.")