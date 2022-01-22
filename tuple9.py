#Counts the number of occurrences of item 50 from a tuple
tuple1 = (50, 10, 60, 70, 50)
size=len(tuple1)
count=0
for i in range(size):
    if tuple1[i]==50:
        count=count+1
print(count)