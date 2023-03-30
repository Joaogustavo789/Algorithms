def find_duplicate(nums):
    if len(nums) <= 1:
        return False

    nums.sort()

    for repeat in range(len(nums)):
        if not isinstance(nums[repeat], int) or nums[repeat] < 0:
            return False

        decrement = repeat - 1

        if nums[repeat] == nums[decrement]:
            return nums[repeat]

    return False

    # print(nums)
    # for repeat in nums:
    #     if not isinstance(repeat, int) or repeat < 0:
    #         return False

    #     # if nums.count(repeat) > 1:
    #     #     # print(repeat)
    #     #     return repeat

    #     # return True

    # return False
