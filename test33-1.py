def while_fuc (start_number,step, top_number):
    my_list=[]
    while start_number < top_number:
        my_list.append(start_number)

        start_number += step
    return my_list

user_enter=raw_input("Pease enter the start number,step and top numbers[a,b,c]:")
user_enter_list= [int(i) for i in user_enter.split(',')]

print while_fuc(user_enter_list[0],user_enter_list[1],user_enter_list[2])
x
