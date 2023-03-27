def is_palindrome_recursive(word, low_index, high_index):
    # print(word)
    # print(low_index)
    # print(high_index)

    if len(word) == 0:
        return False

    elif len(word) == low_index and len(word) == high_index:
        return True

    else:
        return is_palindrome_recursive(word, low_index, len(word) - 1)
