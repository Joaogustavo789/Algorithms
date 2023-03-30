def find_duplicate(nums):
    if len(nums) <= 1:
        return False

    # print(nums)
    for repeat in nums:
        if not isinstance(repeat, int):
            return False

        if repeat < 0:
            return False
    # print(repeat)!
