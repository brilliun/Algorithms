# You are given an array of N integers, A1, A2 ,…, AN. Return maximum value of f(i, j) for all 1 ≤ i, j ≤ N.
# f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.

# For example,

# A=[1, 3, -1]

# f(1, 1) = f(2, 2) = f(3, 3) = 0
# f(1, 2) = f(2, 1) = |1 - 3| + |1 - 2| = 3
# f(1, 3) = f(3, 1) = |1 - (-1)| + |1 - 3| = 4
# f(2, 3) = f(3, 2) = |3 - (-1)| + |2 - 3| = 5

# So, we return 5.

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
# pattern a: A[i] + i - (A[j] + j) , i > j and A[i] > A[j]
# pattern b: A[i] - i - (A[j] - j) , i < j and A[i] > A[j]
        if not A:
            return 1
        min_a, max_a = float("inf"), -float("inf")
        
        for i in range(len(A)):
            val = A[i] + i
            if val > max_a:
                max_a = val
            if val < min_a:
                min_a = val
        
        max_res = max_a - min_a
        
        min_a, max_a = float("inf"), -float("inf")
        
        for i in range(len(A)):
            val = A[i] - i
            if val > max_a:
                max_a = val
            if val < min_a:
                min_a = val
                
        return max(max_res, (max_a - min_a))
