def is_palindrome_iterative(word):
    if len(word) == 0:
        return False

    start_word = 0
    end_word = len(word) - 1

    while start_word < end_word:
        if word[start_word] != word[end_word]:
            return False

        start_word = start_word + 1

        end_word = end_word - 1

    return True

# A R A R A
# s       e
#  s    e
#    se
# Aqui "s" e "e" são iguais, com isso o laço while é encerrado.
