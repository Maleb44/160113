def bin_to_dec(number):
    total = 0
    for i in range(len(number)):
        value = number[len(number) - 1 - i]
        factor = 2 ** i
        total += factor * int(value)

    return total


def bin_to_dec2(number):
    total = 0
    number = number[::-1]
    for i in range(len(number)):
        value = number[i]
        factor = 2 ** i
        total += factor * int(value)

    return total


def bin_to_dec3(number):
    total = 0
    number = number[::-1]
    for i, value in enumerate(number):
        factor = 2 ** i
        total += factor * int(value)

    return total


def bin_to_dec4(number):
    total = 0
    factor = 1
    number = number[::-1]
    for i, value in enumerate(number):
        total += factor * int(value)
        factor *= 2

    return total


def bin_to_dec_rec(number):
    if len(number) == 1:
        return int(number)
    else:
        return 2 ** (len(number) - 1) * int(number[0]) \
            + bin_to_dec_rec(number[1:])

print bin_to_dec('101111')
print bin_to_dec2('101111')
print bin_to_dec3('101111')
print bin_to_dec4('101111')
print bin_to_dec_rec('101111')



