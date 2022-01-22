from audioop import reverse


list1 = [10, 20, 30, 40, 50]
rev_list=reversed(list1)
for i in (rev_list):
    print(i)


print('-----------')
list2=[100,200,300,400,500]
len=len(list2)-1

for i in range(len,-1,-1):
    print(list2[i])

