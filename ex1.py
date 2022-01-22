# Reverse each word of a string



def rev_fun(str):
    words=str.split(" ")
    words_list=(word[::-1] for word in words )

    res=' '.join(words_list)
    return res



str = 'My Name is Jessa'
result=rev_fun(str)
print(result)
