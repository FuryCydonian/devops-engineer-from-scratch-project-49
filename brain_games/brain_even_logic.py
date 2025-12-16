import random

from brain_games.cli_even import getting_answer, welcome_user_and_getting_name


def brain_even_logic():
    name = welcome_user_and_getting_name()
    brain_even_main_logic(name, getting_answer)


def brain_even_main_logic(name: str, function_for_getting_answer):
    """
    Docstring for brain_even_main_logic
    
    :param name: user name
    :type name: str
    :param function_for_getting_answer: function with question and answer
    :type function_for_getting_answer: function
    """
    number_of_attempts = 3
    counter = 0
    for _ in range(number_of_attempts):
        number_for_checking = random.randint(1, 100)
        answer = function_for_getting_answer(number_for_checking)
        if is_correct_user_answer(number_for_checking, answer):
            print("Correct!")
            counter += 1
        else:
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was '{'yes' if is_even(number_for_checking) else 'no'}'."
            )
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")


def is_correct_user_answer(number_for_checking: int, answer: str) -> bool:
    if is_even(number_for_checking) and answer == "yes":
        return True
    elif (not is_even(number_for_checking) and answer == "no"):
        return True
    return False


def is_even(number_for_checking: int) -> bool:
    return number_for_checking % 2 == 0
