import random
from brain_games.games.util_functions_for_games import is_correct_user_answer


def brain_even_main_logic(
    user_name: str,
    get_answer,
    show_success_message,
    show_fail_message,
    number_of_attempts
):
    counter = 0
    for _ in range(number_of_attempts):
        number_for_checking = random.randint(1, 100)
        user_answer = get_answer(int(number_for_checking))
        correct_answer = 'yes' if is_even(number_for_checking) else 'no'
        if is_correct_user_answer(correct_answer, user_answer):
            print("Correct!")
            counter += 1
        else:
            show_fail_message(user_name, user_answer, correct_answer)
            return
    show_success_message(user_name)


def is_even(number_for_checking: int) -> bool:
    return number_for_checking % 2 == 0
