import random
from brain_games.games.util_functions_for_games import is_correct_user_answer


# TODO переделать логику так, чтобы все общие вещи были куда-то вынесены,
# а оставалась только логика для игры.
def brain_even_main_logic(
    user_name: str,
    function_for_getting_answer,
    show_success_message_function,
    show_fail_message_function,
    number_of_attempts
):
    """
    Docstring for brain_even_main_logic
    :param name: user name
    :type name: str
    :param function_for_getting_answer: function with question and answer
    :type function_for_getting_answer: function
    """
    counter = 0
    for _ in range(number_of_attempts):
        number_for_checking = random.randint(1, 100)
        user_answer = function_for_getting_answer(int(number_for_checking))
        correct_answer = 'yes' if is_even(number_for_checking) else 'no'
        if is_correct_user_answer(correct_answer, user_answer):
            print("Correct!")
            counter += 1
        else:
            show_fail_message_function(user_name, user_answer, correct_answer)
            return
    show_success_message_function(user_name)


def is_even(number_for_checking: int) -> bool:
    return number_for_checking % 2 == 0
