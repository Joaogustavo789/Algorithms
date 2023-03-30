def find_duplicate(nums):
    if len(nums) <= 1:
        return False

    # print(nums)s
    for repeat in nums:
        if not isinstance(repeat, int) or repeat < 0:
            return False

        if nums.count(repeat) > 1:
            # print(repeat)
            return repeat
        # print(nums.count(repeat))
    return False
