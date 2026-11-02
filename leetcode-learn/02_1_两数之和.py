# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
# 你可以按任意顺序返回答案。
class Solution:
    def twoSum1(self, nums: list[int], target: int) -> list[int]:
        for i, item in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if item + nums[j] == target:
                    return [i, j]

    def twoSum12(self, nums: list[int], target: int) -> list[int]:
            cache = {}
            for i, item in enumerate(nums):
                 if target - item in cache:
                      return [cache[target - item], i]
                 cache[item] = i