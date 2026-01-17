import random
from brain_games.games.util_functions_for_games import is_correct_user_answer


def brain_gcd_main_logic(
    user_name: str,
    get_answer,
    show_success_message,
    show_fail_message,
    number_of_attempts
):
    counter = 0
    for _ in range(number_of_attempts):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        user_answer = get_answer(f"{a} {b}")
        correct_answer = get_gcd(a, b)
        if is_correct_user_answer(correct_answer, user_answer):
            print("Correct!")
            counter += 1
        else:
            show_fail_message(user_name, user_answer, correct_answer)
            return
    show_success_message(user_name)


def get_gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    while b > 0:
        a, b = b, a % b
    return a
