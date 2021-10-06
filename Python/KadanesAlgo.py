"""
Problem - Kaden's Algo 
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Idea -  
1. Look for all positive contiguous segments of the array. 
2. And keep track of maximum sum contiguous segment among all positive segments. 
3. Each time we get a positive-sum compare it with max_so_far and update max_so_far if it is greater than max_so_far.

Test Cases -
1. I/P - [-2,1,-3,4,-1,2,1,-5,4]
    O/P - 6
2. I/P - [1]
    O/P - 1
3. I/P - [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
    O/P - -3
"""




from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        curr_max = nums[0]

        for i in range(1,len(nums)):
            curr_max = max(nums[i], curr_max + nums[i])
            max_so_far = max(max_so_far,curr_max)

        return max_so_far

obj = Solution()
input = list(map(int, input().split()))
print(obj.maxSubArray(input))