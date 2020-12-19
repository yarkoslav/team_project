'''
This module is for level 2
it shows 10 pair of numbers one by one and the user
must choode the position of the happy number to pass the level
'''
import random
import evil_AI_numbers


def second_level() -> bool:
    """
    The function shows 10 pairs of numbers one by one
    and the player cooses the position of the happy number
    in order to make a passcode to pass the level
    """
    passcode = ""
    user_passcode = ""
    for i in range(10):
        pair_of_nums = []
        position = random.randrange(0, 2)
        happynum = evil_AI_numbers.happy_number(100)
        random_number = random.randrange(1, 100)
        while evil_AI_numbers.is_happy(random_number):
            random_number = random.randrange(1, 100)
        pair_of_nums.append("{}){}".format(position, happynum))
        if position == 1:
            position2 = 0
        else:
            position2 = 1
        pair_of_nums.insert(position2, "{}){}".format(position2, random_number))
        position = str(position)
        passcode += position
        print("Select a position of happy number and press Enter:")
        print(*pair_of_nums)
        input_num = str(input())
        if input_num in ('0', '1'):
            user_passcode += input_num
        else:
            print("Wrong number!")
            print("Select a position of happy number and press Enter:")
            print(*pair_of_nums)
            input_num = str(input())
            user_passcode += input_num
    if passcode == user_passcode:
        print("You have discovered the passcode:{}".format(passcode))
        return True
    print("Your passcode is wrong.")
    return False
