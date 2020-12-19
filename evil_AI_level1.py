"""
This module runs the first level of the game.
It prints the coordinates of the secret base if the player solved the tasks.
The tasks are to choose an even or an odd number from four lists.
"""
import random
from evil_AI_numbers import is_even



def first_level() -> bool:
    """
    Returns True if user solved the tasks and False otherwise.
    """
    def even_and_odd(max_num: int, positive: bool) -> tuple:
        """
        Randomly returns a list of 5 numbers and a type of number which a user has to choose.
        """
        evenness = random.choice(['even', 'odd'])
        if not positive:
            min_num = -max_num
        else:
            min_num = -2

        even_number = random.randrange(min_num + 2, max_num - 2, 2)
        odd_number = random.randrange(min_num + 1, max_num - 1, 2)

        if evenness == 'even':
            numbers = [random.randrange(min_num + 1, max_num - 1, 2) for _ in range(4)]
            right_number = even_number
        else:
            numbers = [random.randrange(min_num, max_num, 2) for _ in range(4)]
            right_number = odd_number
        numbers.append(right_number)
        numbers.sort()

        return evenness, numbers


    def right_answer(task: tuple) -> int:
        """
        Returns right the number of the requested type from the list.
        >>> right_answer('even', [35, 36, 39, 45, 55])
        36
        >>> right_answer('odd', [-55, -30, -14, 60, 88])
        -55
        """
        for num in task[1]:
            if task[0] == 'even':
                if is_even(num):
                    answer = num
                    break
            else:
                if not is_even(num):
                    answer = num
                    break
        return answer


    def check_user(task: tuple) -> bool:
        """
        Returns True if user's answer is right and False otherwise.
        """
        user_number = int(input(f'Choose an {task[0]} number from the list: {task[1]}\n'))
        return bool(user_number == right_answer(task))


    first_coordinate_degree = even_and_odd(90, False)
    first_coordinate_minutes = even_and_odd(100000, True)
    second_coordinate_degree = even_and_odd(180, False)
    second_coordinate_minutes = even_and_odd(100000, True)
    check1 = first_coordinate_degree
    check2 = first_coordinate_minutes
    check3 = second_coordinate_degree
    check4 = second_coordinate_minutes

    coordinates = str(right_answer(check1)) + '.' + str(right_answer(check2)) + ', ' + \
        str(right_answer(check3)) + '.' + str(right_answer(check4))
    check1 = check_user(check1)
    check2 = check_user(check2)
    check3 = check_user(check3)
    check4 = check_user(check4)
    result = check1 and check2 and check3 and check4
    if result:
        print(f'The secret base is situated here: {coordinates}')
    return result
