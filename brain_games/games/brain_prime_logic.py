import random
from brain_games.games.util_functions_for_games import is_correct_user_answer


def brain_prime_main_logic(
    user_name: str,
    function_for_show_user_expression_and_getting_user_answer,
    show_success_message_function,
    show_fail_message_function,
    number_of_attempts
):
    counter = 0
    for _ in range(number_of_attempts):
        number_for_checking = random.randint(1, 100)
        user_answer = function_for_show_user_expression_and_getting_user_answer(int(number_for_checking))
        correct_answer = 'yes' if is_prime(number_for_checking) else 'no'
        if is_correct_user_answer(correct_answer, user_answer):
            print("Correct!")
            counter += 1
        else:
            show_fail_message_function(user_name, user_answer, correct_answer)
            return
    show_success_message_function(user_name)


def is_prime(n: int) -> bool:
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
       d += 2
    return d * d > n
