# My Solution 
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    indices = []  # remove this
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:  # if (i != j and nums[i] + nums[j] == target):
                indices.append(i)
                indices.append(j)
                return indices  # return [i, j]


# Optimized Code
def twoSumOpt(nums, target):
    num_to_index = {}
    for i in range(len(nums)):
        if target - nums[i] in num_to_index:
            return [num_to_index[target - nums[i]], i]
        num_to_index[nums[i]] = i
    return []


if __name__ == '__main__':
    # res = twoSum(nums=[2, 77, 11, 15, 7], target=9)
    # res = twoSum(nums=[3, 3], target=6)
    # res = twoSum(nums=[3, 2, 4], target=6)
    # res = twoSumOpt(nums=[3, 2, 4], target=6)
    res = twoSumOpt(nums=[3, 3], target=6)
    print(res)
