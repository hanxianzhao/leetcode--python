'''
打乱一个没有重复元素的数组。
示例:
// 以数字集合 1, 2 和 3 初始化数组。
int[] nums = {1,2,3};
Solution solution = new Solution(nums);
// 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。
solution.shuffle();
// 重设数组到它的初始状态[1,2,3]。
solution.reset();
// 随机返回数组[1,2,3]打乱后的结果。
solution.shuffle();
'''
import random

'''
超过73.44%
'''
class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.list1 = nums
        self.list2 = nums[:]
    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.list2

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        lens = len(self.list1)
        for i in range(lens):
            j = random.randint(i,lens-1)
            self.list1[i],self.list1[j] = self.list1[j],self.list1[i]
        return self.list1