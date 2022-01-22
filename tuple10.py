# Python program to check if all
# elements in a List are same

def ckeckList(tup):

	ele = tup[0]
	chk = True
	
	# Comparing each element with first item
	for item in tup:
		if ele != item:
			chk = False
			break;
			
	if (chk == True): print("Equal")
	else: print("Not equal")			

# Driver Code
tup = (45, 45, 45, 5, )
ckeckList(tup)
