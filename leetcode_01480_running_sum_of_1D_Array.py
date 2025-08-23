#1480. Running Sum of 1d Array
#https://leetcode.com/problems/running-sum-of-1d-array/
#easy

#Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
#Return the running sum of nums.


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        prev_num = 0
        current_sum = 0
        new_nums = []

        for num in nums:
            print ("num =" + str(num))
            current_sum = num + prev_num
            prev_num = current_sum
            print ("current_sum =" + str(current_sum))
            new_nums.append(current_sum)
            print ("new_nums =" + str(new_nums))

        return(new_nums)
