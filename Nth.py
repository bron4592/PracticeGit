NthSum(n):
	sum = 0
	if n == 1:
		exit(0)
	else if n > 1:
		sum += NthSum(n-1)
return sum
		