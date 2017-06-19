class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        max_start = max_end = -1
        start = end = -1
        max_sum = curr_sum = -1

        for i in range(len(A)):
            a = A[i]
            if a < 0:
                if curr_sum > max_sum or (curr_sum == max_sum and end - start > max_end - max_start):
                    max_sum = curr_sum
                    max_start = start
                    max_end = end
                if curr_sum != -1:
                    curr_sum = -1
                    start = end = -1
            else:
                end = i
                if start < 0:
                    start = i
                    curr_sum = a
                else:
                    curr_sum += a

        if curr_sum > max_sum or (curr_sum == max_sum and end - start > max_end - max_start):
            max_sum = curr_sum
            max_start = start
            max_end = end

        return A[max_start:max_end + 1]