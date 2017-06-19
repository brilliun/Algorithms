class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        curr_sum = 0
        max_sum = -float("inf")

        for a in A:
            curr_sum += a
            if curr_sum > max_sum:
                max_sum = curr_sum
            if curr_sum < 0:
                curr_sum = 0


        return max_sum