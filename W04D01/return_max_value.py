def max(iter):
	max1 = float("-inf")
	for i in iter:
		if max1<i:
			max1=i
	return str(max1) + "Maximum Value"
print(max([1,2,8,-1,0,9]))