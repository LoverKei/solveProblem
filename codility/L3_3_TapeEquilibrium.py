def solution(A):
	# write your code in Python 2.7
	aSum = sum(A)
	minB = ""  # None < any integer < any String
	B = 0

	# make list B ==> sum of A[:P-1]
	# ( 0 ~ P-1 ) vs ( P ~ N )
	# ==>       B vs A[P:]
	for P in range(1, len(A)):
		B = B + A[P-1]

		# B = A[:P]
		# B + A[P:] = aSum
		# ==> A[P:] = aSUm - B
		
		# find min
		# ==> (B - A[P:]) ==> B - (aSum - B) ==> B*2 - aSum
		cal = abs(B*2 - aSum)
		if cal < minB:
			minB = cal
	
	return minB
