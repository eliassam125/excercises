"""
This was an exercise from LeetCode

The statement was:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
"""
from itertools import combinations


class Solution(object):
    def threeSum(self, nums):
        combinations_list = list(combinations(nums, 3))
        lista_de_valores = []
        for combo in combinations_list:
            if sum(combo) == 0:
                combo_1 = sorted(combo)
                test_is_in = True
                for alredyinlist in lista_de_valores:
                    if combo_1 == alredyinlist:
                        test_is_in = False
                if test_is_in:
                    lista_de_valores.append(combo_1)
        return sorted(lista_de_valores)

