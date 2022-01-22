
def first_last_same(numbers_list):
    if numbers_list[0]==numbers_list[-1]:
        return True
    else :
        return False


numbers_x=[10,20,30,40,10]
print(numbers_x)
print('result is',first_last_same(numbers_x))

numbers_y=[75,65,35,75,30]
print(numbers_y)
print('result is',first_last_same(numbers_y))


#return function akathu mathrame kodukkan pattullu.
# if statement koode return koduthal error kittum.(error egane verum('return outside function')