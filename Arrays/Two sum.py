class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            f = target - nums[i]
            set1 = nums

            if f in set1 and nums.index(f) != i:
                ind = nums.index(f)
                print(i, ind)
                return [i, ind]
