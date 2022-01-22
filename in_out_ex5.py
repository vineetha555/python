#******************  important   *******


numbers = []

# 5 is the list size
# run loop 5 times
for i in range(0, 5):
    
    # accept float number from user
    item = float(input('enter num:'))
    # add it to the list
    numbers.append(item)

print("User List:", numbers)