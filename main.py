
from typing import List
from itertools import permutations
import itertools


class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        count = 0
        for i, v in enumerate(nums):
            if val != v:
                pass
            else:
                nums = nums[:i]+nums[i+1:]
                count += 1
        [nums.remove(i) for i in nums if i == val]
        lenght = len(nums)
        for i in range(count):
            nums.append("_")
        return lenght

    def nextPermutation(self, nums: List[int]) -> None:
        permutations = (itertools.permutations(nums))
        res = list(permutations)
        nums = list(res[1])
        print(nums)

    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        rangeList = []
        if target not in nums:
            return [-1, -1]

        for i, v in enumerate(nums):
            if target == v:
                rangeList.append(i)
        if len(rangeList) == 1:
            rangeList.append(rangeList[0])
        return [rangeList[0], rangeList[-1]]

    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        nums.append(target)
        nums = sorted(nums)
        print(nums)
        return nums.index(target)

    def permute(self, nums: List[int]) -> List[List[int]]:
        per = permutations(nums)
        result = [list(i) for i in per]
        return result

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        per = permutations(nums)
        res = [list(i) for i in per]
        result = []
        for i in res:
            if i not in result:
                result.append(i)
        return result

    def sortColors(self, nums: List[int]) -> None:
        pass

    def greaterThan(self, nums:List[int], n:int) -> bool:
        return max(nums) <= n
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        com = itertools.combinations([i for i in range(1, n+1)], k)
        return [list(i) for i in com] 

    def subsets(self, nums: List[int]) -> List[List[int]]:
        com = itertools.combinations(nums, 2)

    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        for i, v in enumerate(nums):
            if nums.count(v) > 2:
                self.removeCount(nums, (nums.count(v)-2), v)

        for i in range(length - len(nums)):
            nums.append("_")
        print(nums)
                

    def removeCount(self, nums:List[int], count:int, num:int) -> List[int]:
        for i in range(count):
            nums.remove(num)
        return nums

    def search(self, nums: List[int], target: int) -> bool:
        return target in nums

    def largestRectangleArea(self, heights: List[int]) -> int:
        return max(heights)

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        self.removeElement(nums1, 0)
        nums1 = nums1 + nums2
        return sorted(nums1)


    def removeElement(self, nums: List[int], num:int) -> List[int]:
        for i in nums:
            if i == num:
                for _ in range(nums.count(num)):
                    nums.remove(num)
        return nums

    def maxProfit(self, prices: List[int]) -> int:

        for i in prices:
            
            newls = [n for n in prices[prices.index(i)+1:] ]
            if len(newls)  < 1:
                return 0
            res, length, *z = self.returnMaxindex(i, newls)
            if res == True:
                profit = length - i
                return profit
            else:
                continue


    def returnMaxindex(self, num:int, nums: List[int]) -> tuple:
        
        mx = max(nums)
        if mx > num:
            return(True, mx)
        return (False, 0)
        

    def get_sum(self, a,b):
        sum = 0
        if a > b:
            for i in range(b, a+1):
                print(i)
                sum += i
            return sum
        elif b > a:
            for i in range(a, b+1):
                print(i)
                sum += i
            return sum    
        return a     

    def longest(self, a1, a2):
        alph = a1 + a2
        alph_set = set(alph)
        alph2 = ""

        for i in alph_set:
            if str(i).isalpha():
                alph2 += i
        alph2 = sorted(alph2)
        return "".join(alph2)

    def firstUniqChar(self, s: str) -> int:
        key_value = {}
        for i in s:
            if i in key_value.keys():
                key_value[i] += 1
            else:
                key_value[i] = 1
        print(key_value)
        for i, v in key_value.items():
            if v == 1:
                print(i)
                return s.index(i)
        return -1

    def reverseString(self, s: List[str]) -> None:
        s_str = "".join(s[::-1])
        s = [i for i in s_str]

    def reverse(self, x: int) -> int:
        if abs(x) < 2**31 and not(x >= 2**31 - 1):
            if x < 0:
                ss = list(str(x))
                ss.remove("-")
                s = int("".join(ss[::-1]))
                return - s
            return int(str(x)[::-1])
        return 0
    def check_32_bit(self, n):
        return n<1<<31

    def up_array(self, arr):
        if arr == [] and all([True if int(i) > 0 <= 9 else False for i in str(arr)]): return 0
        sum = int("".join([str(i) for i in arr])) + 1
        return [int(i) for i in str(sum)]
        
    def sort(self, iter, descending=False):
        newIter = []

        # sort list in descending order
        if descending == True:
            for _ in range(len(iter)):
                maxValue = reduce(lambda x, y: x if x > y else y, iter)
                iter.remove(maxValue)
                newIter.append(maxValue)

        # sort list in ascending order
        for _ in range(len(iter)):
            minValue = reduce(lambda x, y: x if x < y else y, iter)
            iter.remove(minValue)
            newIter.append(minValue)
        return newIter
list_a = (5, 2, 3, 8, 10 ,1, 2)
#https://jobtensor.com/Tutorial/Python/en/Map-Filter-Reduce

# find largest value in an iterable

print(reduce(lambda x, y: x if x > y else y, list_a))

# find small value in an iterable

print(reduce(lambda x, y: x if x < y else y, list_a))

# alternative zip function
print(list(map(lambda x, y: (str(x), y), "abcd", [1, 2, 3])))



s = Solution()
print(s.up_array([4, 3, 9, 9])) 