# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(X, A):
    # write your code in Python 2.7

    # find small idx 1 to X in A
    # Goal : Time Complexity - O(N), Space Complextity - O(X)

    # make no duplication A
    B = [0] * (X + 1)
    cnt = 0
    for i in range(len(A)):
        if B[A[i]] == 0:
            B[A[i]] = A[i]
            cnt += 1
            if cnt == X:
                return i

    return -1

    pass

if __name__ == "__main__":
    print( solution(5, [1,3,1,4,2,3,5,4]))
    print( solution(5, [-1]))
