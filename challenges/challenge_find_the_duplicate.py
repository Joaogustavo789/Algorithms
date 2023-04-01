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
