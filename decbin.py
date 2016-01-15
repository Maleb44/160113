def dec_to_bin_rec(number):
    quotient = number // 2
    remainder = number % 2

    if quotient == 0:
        return str(number)
    else:
        return dec_to_bin_rec(quotient) + str(remainder)


def dec_to_bin_andi(number):
    szam = []
    while number > 0:
        quotient = number // 2
        remainder = number % 2

        szam.insert(0, str(remainder))
        number = quotient
    return ''.join(szam)



print dec_to_bin_rec(47)
print dec_to_bin_andi(47)







# 47 = 23*2 + 1
# 23 = 11*2 + 1
# 11 = 5*2 + 1
#  5 = 2*2 + 1
#  2 = 1*2 + 0
#  1 = 0*2 + 1


# 47 = (((((1)*2 + 0)*2 + 1)*2 + 1)*2 + 1) *2 + 1

# '101111'
