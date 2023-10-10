# Given a binary array nums, return the maximum number of consecutive 1's in the array.
# Example 1:
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:
# Input: nums = [1,0,1,1,0,1]
# Output: 2

# def solution(nums):
#     consecutive_nums = 0
#     max_consecutive = 0
#     for num in nums:
#         if num:
#             consecutive_nums += 1
#         else:
#             if consecutive_nums > max_consecutive:
#                 max_consecutive = consecutive_nums
#             consecutive_nums = 0
#     if consecutive_nums > max_consecutive:
#         max_consecutive = consecutive_nums
#     return max_consecutive

def solution(given_nums):
    num_count = 0
    consecutive_count = []
    for num in given_nums:
        if num == 1:
            num_count += 1
        else:
            consecutive_count.append(num_count)
            num_count = 0
    consecutive_count.append(num_count)
    return max(consecutive_count)
            