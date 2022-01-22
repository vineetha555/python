

def merge_list(list1,list2):
    result_list=[]

    for i in list1:
        if (i%2==0):
            result_list.append(i)

    for i in list2:
        if (i%2!=0):
            result_list.append(i)

    return result_list

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
final_output=merge_list(list1,list2)
print(final_output)