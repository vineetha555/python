def outer_func(a,b):
    def addition(a,b):
        sum=a+b
        return  sum

    sum =addition(a,b)
    return sum + 5

final_result=outer_func(5,5)
print(final_result)






