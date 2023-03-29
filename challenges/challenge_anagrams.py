def is_anagram(first_string, second_string):
    string_lower1 = first_string.lower()
    string_lower2 = second_string.lower()
    # print(string_lower1, string_lower2)
    sort_merge1 = merge_sort(string_lower1)
    sort_merge2 = merge_sort(string_lower2)

    assemble_sort1 = "".join(sort_merge1)
    assemble_sort2 = "".join(sort_merge2)

    if len(sort_merge1) == 0 or len(sort_merge2) == 0:
        return (assemble_sort1, assemble_sort2, False)
    # print(sort_merge1)
    # print(sort_merge2)

    if assemble_sort1 == assemble_sort2:
        return (assemble_sort1, assemble_sort2, True)

    return (assemble_sort1, assemble_sort2, False)


def merge_sort(words):
    # print(words)
    if len(words) <= 1:
        return words

    mid = len(words) // 2
    left = merge_sort(words[:mid])
    right = merge_sort(words[mid:])

    return merge(left, right, words)


def merge(left_word: list, right_word, merged):
    le_li = list(left_word)
    ri_li = list(right_word)
    merged_li = list(merged)
    left_word_idx, right_word_idx = 0, 0

    while left_word_idx < len(le_li) and right_word_idx < len(ri_li):
        if ord(le_li[left_word_idx]) <= ord(ri_li[right_word_idx]):
            merged_li[left_word_idx + right_word_idx] = le_li[left_word_idx]
            left_word_idx += 1
        else:
            # print(merged_li)
            merged_li[left_word_idx + right_word_idx] = ri_li[right_word_idx]
            right_word_idx += 1

    for left_word_idx in range(left_word_idx, len(le_li)):
        merged_li[left_word_idx + right_word_idx] = le_li[left_word_idx]

    for right_word_idx in range(right_word_idx, len(ri_li)):
        merged_li[left_word_idx + right_word_idx] = right_word[right_word_idx]

    return merged_li


# roma
# amor

# merge_sort

# 35287916
# 3 5 2 8 || 7 9 1 6
# 3 5 || 2 8 || 7 9 || 1 6
# 3 5 2 8 7 9 1 6

# merge

# 3 5 2 8 7 9 1 6
# 3 5 || 2 8 || 7 9 || 1 6
# 3 5 2 8 || 7 9 1 6
# 1 2 3 5 6 7 8 9
