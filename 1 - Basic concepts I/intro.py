def peak1(A):
    if A[0]>=A[1]: return 0
    for i in range(1, len(A)-1):
        if A[i]>=A[i-1] and A[i]>=A[i+1]: return i
    if A[-1]>=A[-2]: return len(A)-1
    else:
        return None

def findmax(A):
    m = A[0]
    r = 0
    for i in range(1, len(A)):
        if A[i] >= m:
            m = A[i]
            r = i
    return r 

import math

def peak3(A, i, j):
    m = math.floor((i+j)/2)
    # Check if (A only has one element) or (A has two elements) or I=(A has > 2 elements)
    if (len(A)==1) or(A[m] >= A[m+1]) or (A[m] >= A[m+1] and A[m] >= A[m-1]): return m
    elif A[m-1]>=A[m]: return peak3(A, i, m-1)
    else: return peak3(A, m+1, j)

