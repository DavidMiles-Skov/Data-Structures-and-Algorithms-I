n = int(input())
s = input()
A = [int(i) for i in s.split()]

def get_max_sub_arr(A):
    m = A[0]
    for i in range(0, len(A)):
        curr_sum = 0
        for j in range(0, len(A)):
            curr_sum += A[j]
            if curr_sum > m: m = curr_sum
    return m
