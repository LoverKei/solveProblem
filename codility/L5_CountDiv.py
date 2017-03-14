def solution(A, B, K):
	# write your code in Python 2.7

	# [A1, A2, ..., A-1, A, A+1 , ... B]
	# len( A to B  mod K == 0)  - len( A1 to A-1 mod K == 0)

	return int(B/K) - int( (A-1)/K )
	pass

