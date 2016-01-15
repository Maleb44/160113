
def a():
    b()


def b():
    try:
        c()
    except ValueError:
        print 'error'


def c():
    d()


def d():
    raise ValueError('ohhh')


try:
    a()
except ValueError, KeyError:  # Exception -> everything
    print 'any possible exception'

from math import sqrt


# return tuple

def my_sqrt_classic(number):
    if number < 0:
        return False, 0

    return True, sqrt(number)

my_num = -3
success, value = my_sqrt_classic(my_num)

if success:
    print value
else:
    print 'number not valid'


# raise

def my_sqrt_raise(number):
    assert number >= 0
    sqrt(number)


try:
    my_sqrt_raise(my_num)
except AssertionError:
    print 'number not valid'



# if
next_player = 0
if next_player == 1:
    next_player = 2
else:
    next_player = 1

print 'next_player: ' + str(next_player)    

# lookup dict
lookup_next_player = {
    1: 2,
    2: 1
}
next_player = lookup_next_player[next_player]

# lookup list
lookup_next_player = [0, 2, 1]
next_player = lookup_next_player[next_player]
