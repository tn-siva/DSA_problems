def twoSum(self, nums: List[int], target: int) -> List[int]:
    for ind in range(len(nums)):
        ans = []
        ans.append(ind)

        if nums[ind] == target:
            a = nums[ind]
            nums[ind] = 10000001
            ans.append(nums.index(0))
            return ans

        print(target)
        print(nums[ind])
        rem = target-nums[ind]
        nums[ind] = 10000001
        if rem in nums:
            ans.append(nums.index(rem))
            return ans


def twoSumHashMap(self, nums: List[int], target: int) -> List[int]:
    hmap = {}
    for ind, val in enumerate(nums):
        diff = target - val
        if diff in hmap:
            return [hmap[diff], ind]
        hmap[val] = ind
