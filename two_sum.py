# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]

# Intuition: Use a cache to store one number on an iteration, see if number + any other numbers = target; I want to avoid a nested loop
# After evaluating the above, I don't think this is a good solution because it has O(n log n) time complexity due to needing to first recursively divide the array, then merge it after fully divided. The simpler solution is to use a hash map, as below

def twoSum(nums, target):
    prev_map = {}
    for i, num in enumerate(nums):
        answer = target - num
        if answer in prev_map:
            return [prev_map[answer], i]
        prev_map[num] = i
    