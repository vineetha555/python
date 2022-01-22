s1='America'
s2='Japan'
x=s1[0]+s2[0]
mi=int(len(s1)/2)
mi2=int(len(s2)/2)
x=x+s1[mi]+s2[mi2]+s1[-1]+s2[-1]
print(x)
