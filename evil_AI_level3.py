'''
This module provides the gameplay of 3 level in game,
in which player must find the password(in letters) to
the door, behind which is artificial inteligence
'''
import random
import evil_AI_numbers


def generate_grid() -> list:
    '''
    Return the list of twenty numbers, all of them are <= 26
    (because we turn our numbers into letters when we decode password)
    e.g. [13, 17, 25, 5, 8, 20, ... , 7, 16]
    '''
    grid = []
    while len(grid) <= 20:
        grid.append(random.randint(1, 26))
    return grid


def num_into_letter(num: int) -> str:
    '''
    Return the corresponding alphabet letter

    >>> num_into_letter(1)
    'a'
    >>> num_into_letter(26)
    'z'
    '''
    letter = chr(ord('a') + num - 1)
    return letter


def third_level() -> bool:
    '''
    This function ran the third level, in which player must
    find out and write all Ulam numbers from the grid, and our
    program makes the user password from numbers, which user wrote
    before. The level is passed if user password is equal to correct
    password and our function return True in this case.
    '''
    print('Select Ulam numbers from the list in the same order as their appearance.')
    print('After each number press Enter and you will receive corresponding alphabet letter.')
    print('The string of those letters is password,'
    ' when there are no Ulam numbers left, write the password.\n')
    grid = generate_grid()
    print(grid)
    correct_password = []
    for num in grid:
        if evil_AI_numbers.is_ulam(num):
            correct_password.append(num_into_letter(int(num)))
    correct_password = ''.join(correct_password)
    while True:
        line = input()
        try:
            user_num = int(line)
            print(num_into_letter(user_num))
        except ValueError:
            user_password = line
            break
    if user_password == correct_password:
        print(f'Your password {user_password} is correct')
        is_level_passed = True
    else:
        print(f'Your password {user_password} is incorrect')
        print(f'Correct password is {correct_password}')
        is_level_passed = False
    return is_level_passed
