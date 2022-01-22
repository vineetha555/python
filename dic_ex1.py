keys=['ten','twenty','thirty']
values=[10,20,30]

new_dic=dict()
for i in range(len(values)):
        new_dic.update({keys[i]:values[i]})

print(new_dic)