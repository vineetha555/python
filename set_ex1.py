sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]
list2=list(sample_set)
res=(list2+sample_list)
final_res=set(res)
print(final_res)

#method 2-------
res1=set(sample_list)
fi=sample_set|res1
print(fi)

#method 3------
sample_set.update(sample_list)
print(sample_set)