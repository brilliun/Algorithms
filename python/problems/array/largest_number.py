# Given a list of non negative integers, arrange them such that they form the largest number.

# For example:

# Given [3, 30, 34, 5, 9], the largest formed number is 9534330.

# Note: The result may be very large, so you need to return a string instead of an integer.


class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        if not A:
            return ''
        
        result = []
        idx = 0
        A = sorted((str(a) for a in A), reverse=True)
        for i in range(0, len(A)):
            curr = A[i]
            if curr == '0' and idx == 0:
                continue
            j = idx - 1
            while j > -1:
                if (curr + result[j]) > (result[j] + curr):
                    j = j - 1
                else:
                    result.insert(j + 1, curr)
                    break
            if j == -1:
                result.insert(0, curr)
            
            idx += 1
            
        
        if not result:
            return '0'
        return ''.join(str(x) for x in result)
