tuple1 = (10, 20, 30, 40, 50)
len=len(tuple1)
for i in range(len-1,-1,-1):
    print(tuple1[i])



    #method 2 

tuple2=tuple1[::-1]
print(tuple2)