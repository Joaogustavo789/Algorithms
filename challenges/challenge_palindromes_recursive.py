def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0:
        return False

    elif low_index >= high_index:
        return True

    elif word[low_index] != word[high_index]:
        return False

    else:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)

# A R A R A
# 0 1 2 3 4
# i       j
#   i   j
#     ij
# Aqui retorna True, pois i = A e j = A são iguais

# O S S O
# 0 1 2 3
# i     j
#   i j
#   j i
# Aqui retorna True, pois i é maior que j e i = S e j = S

# A G U A
# 0 1 2 3
# i     j
#   i j
#   j i
# Aqui retorna False, pois G e U são diferentes
