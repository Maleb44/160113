def split_words(sentence):
    word_list = sentence.split()
    return word_list


def reverse_words(list_str):
    reversed_list = list()
    for word in list_str:
        reversed_word = reverse_one_word(word)
        reversed_list.append(reversed_word)
    return reversed_list


def reverse_one_word(word):
    # word
    rev = word[::-1]

    # punctuation marks
    if not rev[0].isalpha():
        rev = rev[1:] + rev[0]

    # lowercase-uppercase
    if word[0].isupper():
        rev = rev.capitalize()

    return rev


def join_list(list_str):
    return ' '.join(list_str)


def exercise(sentence):
    splitted = split_words(sentence)
    reversed_list = reverse_words(splitted)
    joined = join_list(reversed_list)
    return joined


input = 'Thank you so much, Andrew!'
print input
print exercise(input)








