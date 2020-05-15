import re

def ADD(a,b):
    print "%d+%d=%d " % (a,b,a+b)

def SUBTRACT(a,b):
    print "%d-%d=%d " % (a,b,a-b)

def MULTIPLY(a,b):
    print "%d*%d=%d " % (a,b,a*b)

def DIVIDE(a,b):
    if b==0:
        print "Please enter in correct format."
    else:
        print "%d/%d=%d " % (a,b,a/b)


go_on="yes"

while go_on!="no":

    user_enter=raw_input("Please enter [eg: x+y]: ")
    user_number=[int(s) for s in re.findall(r'\d+',user_enter)]

    if "+" in user_enter:
        ADD(user_number[0],user_number[1])
    elif "-" in user_enter:
        SUBTRACT(user_number[0],user_number[1])
    elif "*" in user_enter:
        MULTIPLY(user_number[0],user_number[1])
    elif "/" in user_enter:
        DIVIDE(user_number[0],user_number[1])
    else:
        print "Please enter in correct format."

    go_on=raw_input("Do you want to go on? [yes or no]: ")
