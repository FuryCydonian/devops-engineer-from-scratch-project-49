import random
from brain_games.games.util_functions_for_games import is_correct_user_answer


def brain_calc_main_logic(
    user_name: str,
    get_answer,
    show_success_message,
    show_fail_message,
    number_of_attempts
):
    counter = 0
    for _ in range(number_of_attempts):
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        operator = random.choice(["+", "-", "*"])
        math_expression_as_text = math_expression_to_string(x, y, operator)
        math_expression = get_math_expression(x, y, operator)
        user_answer = get_answer(math_expression_as_text)
        correct_answer = math_expression(_)
        if is_correct_user_answer(correct_answer, user_answer):
            print("Correct!")
            counter += 1
        else:
            show_fail_message(user_name, user_answer, correct_answer)
            return
    show_success_message(user_name)


def get_math_expression(x: int, y: int, operator: str):
    match operator:
        case "+":
            return lambda _: x + y
        case "-":
            return lambda _: x - y
        case "*":
            return lambda _: x * y


def math_expression_to_string(x: int, y: int, operator: str):
    return f"{x} {operator} {y}"
