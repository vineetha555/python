list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

# list[0]=10
# list[1]=20
# list[2][2]=7000
# list[3]=30
# list[4]=40

list1[2][2].append(7000)
print(list1)