import sys

stack = []
for i in range(9):
    stack.append("")
stackptr = 0
menuchoice = 0
def cmdPop_click(stack, stackptr):
    if stackptr < 1:
        print("Underflow")
        return stackptr
    stackptr = stackptr - 1
    print(stack[stackptr])
    return stackptr

def cmdPush_click(stack, stackptr):
    newval = input("Enter new value: ")
    if stackptr > 9:
        print("overflow")
        return stackptr
    stack[stackptr]=newval
    stackptr+=1
    return stackptr


while menuchoice != 3:
    print("1. To PUSH to STACK\n2. To POP from STACK\n3. To exit this module.")
    menuchoice = int(input())
    if menuchoice == 1:
        stackptr = cmdPush_click(stack, stackptr)
    elif menuchoice == 2:
        stackptr = cmdPop_click(stack, stackptr)
    elif menuchoice == 3:
        sys.exit()
    else:
        print("Wrong choice. Please try again.")
