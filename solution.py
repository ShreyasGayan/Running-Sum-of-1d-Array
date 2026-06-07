class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = list()
        count = nums[0]
        for index, i in enumerate(nums):
            if index == 0:
                ans.append(nums[index])
            elif index > 0:
                ans.append(nums[index]+count)
                count += nums[index]
        return ans