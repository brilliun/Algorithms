# Given an unsorted integer array, find the first missing positive integer.

# Example:

# Given [1,2,0] return 3,

# [3,4,-1,1] return 2,

# [-8, -7, -6] returns 1

# Your algorithm should run in O(n) time and use constant space.

class Solution:
    # @param A : list of integers
    # @return an integer
    # 2, 4, 6, 8, 10, 1, 3
    def firstMissingPositive(self, A):
        if not A:
            return 1
    
        max_a = len(A)
        i = 0
        while i < max_a:
            a = A[i]
            if a > 0 and a <= max_a and i != a - 1 and A[i] != A[a - 1]:
                A[i], A[a - 1] = A[a - 1], A[i]
            else:
                i += 1
                
        i = 0
        for i in range(0, max_a):
            if A[i] != i + 1:
                return i + 1
        
        return max_a + 1
