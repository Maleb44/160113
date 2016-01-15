def my_sqrt_classic(number):
    if number < 0:
        return False, 0

    return True, sqrt(number)


my_num = -3
success, value, d1 = my_sqrt_classic(my_num)

if success:
    print value
else:
    print 'number not valid'
   