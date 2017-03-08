# Use python dict type.

def solution(A):
	min = 2147483647
	max = 0

	B = {} # dictionary data structure B (like HashMap)

	for i in A:
		B[i] = "True"
		if i > 0 and i < min:
			min = i
		if i > max:
			max = i

	if min > 1 or min > max:
		return 1
	
	for i in range(min+1, len(B) + min+1):
		if B.get(i, None) == None:
			return i
