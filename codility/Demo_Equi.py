def solution(A):
	# write your code in Python 2.7
	B = 0
	sumA = sum(A)

	for P in range(0, len(A)):
		if B == sumA - A[P] - B:
			return P

		B+= A[P]

	return -1
