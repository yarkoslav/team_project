'''
This module provides all operations with our types of numbers
(even,happy,Ulam numbers), which are used in our game
There are two types of functions: 1) generate a sequence or random number
from sequence
2) check is number in sequence
'''
import random


def ulam_sequence(num: int) -> list:
    '''
    Return the list of all Ulam's numbers, which are <= num

    >>> ulam_sequence(1)
    [1]
    >>> ulam_sequence(2)
    [1, 2]
    >>> ulam_sequence(25)
    [1, 2, 3, 4, 6, 8, 11, 13, 16, 18]
    '''
    if num == 1:
        sequence = [1]
    elif num == 2:
        sequence = [1, 2]
    else:
        sequence = [1, 2]
        count_sums = [0 for i in range(2 * num)]
        count_sums[2] = 1
        new_number = 3
        while new_number <= num:
            if count_sums[new_number - 1] == 1:
                for ulam_num in sequence:
                    new_sum = ulam_num + new_number
                    count_sums[new_sum - 1] += 1
                sequence.append(new_number)
            new_number += 1
    return sequence


def is_ulam(num: int) -> bool:
    '''
    Return True if num is Ulam number, otherwise return False

    >>> is_ulam(1)
    True
    >>> is_ulam(26)
    True
    >>> is_ulam(24)
    False
    '''
    return bool(num in ulam_sequence(num))


def happy_number(num: int) -> int:
    """
    Returns a random happy number that is less
    than the given one
    e.g. happy_number(36) = 10
    """
    random_number = random.randrange(1, num)
    while is_happy(random_number) is None or not is_happy(random_number):
        random_number = random.randrange(1, num)
    return random_number


def is_happy(num: int) -> bool:
    """
    Finds out if the given number is happy or not
    >>> is_happy(97)
    True
    >>> is_happy(78)
    False
    """
    check = False
    if num % 10 == num:
        num = num ** 2
        if num == 1:
            check = True
    while num % 10 != num and not check:
        num = str(num)
        new_num = 0
        for digit in num:
            new_num += int(digit) ** 2
        num = new_num
        if num == 1:
            check = True
        elif num % 10 == num:
            break
    return check


def is_even(num: int) -> bool:
    """
    Returns True if the number num is even.
    >>> is_even(5)
    False
    >>> is_even(46)
    True
    """
    return bool(num % 2 == 0)
