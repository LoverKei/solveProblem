# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(N, A):
    # write your code in Python 2.7

    # Goal : TimeComplexity O(N+M) , SpaceComplexity O(N)

    maxCounter = 0        # always MaxCounter
    oldMaxCounter = 0     # before A[K] == N+1, maxCounter
    B = [0] * N

    for K in range(len(A)):
        # if A[K] > N+1, Error input...
        if A[K] > N+1 or A[K] < 1:
            continue

        # if A[K] = X , 1 <= X <= N
        elif A[K] < N+1:
            if B[A[K]-1] < oldMaxCounter:
                B[A[K]-1]  =  oldMaxCounter + 1  
            else :
                B[A[K]-1] += 1

            if maxCounter < B[A[K]-1]:
                maxCounter = B[A[K]-1]
        
        # if A[K] = N+1 , K is max Counter
        else :
            # B[ALL] = maxCounter
            # O(N+M)? 
            oldMaxCounter = maxCounter

    for i in range(len(B)):
        if B[i] < oldMaxCounter:
            B[i] = oldMaxCounter
    return B
    pass




if __name__ == "__main__":
    print( solution(5, [3,4,4,6,1,4,4]) )
    print( solution(5, [3,4,4,6,1,4,4,3,4,4,6,1,4,4,3,4,4,6,1,4,4,3,4,4,6,1,4,4,3,4,4,6,1,4,4,3,4,4,6,1,4,4,3,4,4,6,1,4,4,3,4,4,6,1,4,4,3,4,4,6,1,4,4,3,4,4,6,1,4,4,3,4,4,6,1,4,4,3,4,4,6,1,4,4]))
    print( solution(1000, [3,4,5,6,4,3,2,1,1,2,2,23,3,12,2,1,2,31,21,123,12,31,1,1,1,1,1,100,3,34,5,5,6,5,4,4,3]))
