# Calculate the sum and average of the digits present in a string


str1 = "PYnative29@#8496"
total=0
count=0
for i in str1:
    if i.isdigit():
        total= total+int(i)
        count= count + 1

avg = total /count

print('total:',total,'avg:',avg)