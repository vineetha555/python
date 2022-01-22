# Count all letters, digits, and special symbols from a given string


str1 = "P@#yn26at^&i5ve"

letters=0
digits=0
special_symbols=0
for char in str1:
    if char.isalpha():
        letters+=1

    elif  char.isdigit():
        digits+=1

    else :
        special_symbols+=1

print('letters count:',letters,' digits:',digits,'special_symbols:',special_symbols)


