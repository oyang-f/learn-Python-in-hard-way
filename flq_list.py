list_len=range(0,int(raw_input("Please input the list lenght(>+3):")))
i=0
j=0
flq_list=[]
print list_len

while i in list_len:
    j=i+1
    if j==1:
        flq_list.append(1)
    elif j==2:
        flq_list.append(1)
    else:
        flq_list.append(flq_list[j-2]+flq_list[j-1])

print flq_list
