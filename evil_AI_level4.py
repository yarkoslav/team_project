"""
This module contains 4th level of the game.
The user should choose from the given 5 lists right number.
"""
import random
import evil_AI_numbers


def none_prop() -> list:
    """
    Return list of numbers with no properties.
    """
    suitable_numbers = []
    for i in range(1, 100):
        if not evil_AI_numbers.is_even(i) and not evil_AI_numbers.is_happy(i) and \
           not evil_AI_numbers.is_ulam(i):
            suitable_numbers.append(i)
    return suitable_numbers


def even_and_happy() -> list:
    """
    Return list of even and happy numbers.
    """
    suitable_numbers = []
    for i in range(1, 100):
        if evil_AI_numbers.is_even(i) and evil_AI_numbers.is_happy(i):
            suitable_numbers.append(i)
    return suitable_numbers


def even_and_ulam() -> list:
    """
    Return list of even and ulam numbers.
    """
    suitable_numbers = []
    for i in range(1, 100):
        if evil_AI_numbers.is_even(i) and evil_AI_numbers.is_ulam(i):
            suitable_numbers.append(i)
    return suitable_numbers


def happy_and_ulam() -> list:
    """
    Return list of happy and ulam numbers.
    """
    suitable_numbers = []
    for i in range(1, 100):
        if evil_AI_numbers.is_happy(i) and evil_AI_numbers.is_ulam(i):
            suitable_numbers.append(i)
    return suitable_numbers


def all_prop() -> list:
    """
    Return list of numbers that hape all three properties.
    """
    suitable_numbers = []
    for i in range(1, 100):
        if evil_AI_numbers.is_even(i) and evil_AI_numbers.is_happy(i) and \
           evil_AI_numbers.is_ulam(i):
            suitable_numbers.append(i)
    return suitable_numbers


def create_output_list(lst_right_numbers: list) -> list:
    """
    Return output list with only incorrect answers.
    """
    output_list = []
    all_wrong_numbers = []
    for i in range(1, 100):
        if i not in lst_right_numbers:
            all_wrong_numbers.append(i)
    for _ in range(4):
        output_list.append(random.choice(all_wrong_numbers))
    return output_list


def right_answer(lst_right_numbers: list) -> int:
    """
    Return right answer (number).
    """
    right_number = random.choice(lst_right_numbers)
    return right_number


def fourth_level() -> bool:
    """
    Return True if the answer is right and False is it is not.
    """
    list_of_properties = ['None', 'Even & Happy', 'Even & Ulam', 'Happy & Ulam', 'All']
    random.shuffle(list_of_properties)
    users_life = True
    for random_prop in list_of_properties:
        if random_prop == 'None':
            print("Choose the number that isn't even or happy or Ulam:")
            output_list = create_output_list(none_prop())
            right_number = right_answer(none_prop())
            output_list.append(right_number)
            random.shuffle(output_list)
            print(output_list)
            answer = int(input())
            if answer != right_number:
                users_life = False

        elif random_prop == 'Even & Happy':
            print("Choose the number that is both even and happy:")
            output_list = create_output_list(even_and_happy())
            right_number = right_answer(even_and_happy())
            output_list.append(right_number)
            random.shuffle(output_list)
            print(output_list)
            answer = int(input())
            if answer != right_number:
                users_life = False

        elif random_prop == 'Even & Ulam':
            print("Choose the number that is both even and Ulam:")
            output_list = create_output_list(even_and_ulam())
            right_number = right_answer(even_and_ulam())
            output_list.append(right_number)
            random.shuffle(output_list)
            print(output_list)
            answer = int(input())
            if answer != right_number:
                users_life = False

        elif random_prop == 'Happy & Ulam':
            print("Choose the number that is both Ulam and happy:")
            output_list = create_output_list(happy_and_ulam())
            right_number = right_answer(happy_and_ulam())
            output_list.append(right_number)
            random.shuffle(output_list)
            print(output_list)
            answer = int(input())
            if answer != right_number:
                users_life = False

        elif random_prop == 'All':
            print("Choose the number that is even, happy and Ulam:")
            output_list = create_output_list(all_prop())
            right_number = right_answer(all_prop())
            output_list.append(right_number)
            random.shuffle(output_list)
            print(output_list)
            answer = int(input())
            if answer != right_number:
                users_life = False

    return users_life
