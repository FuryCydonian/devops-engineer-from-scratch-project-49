import random
from brain_games.games.util_functions_for_games import is_correct_user_answer


# TODO изменить логику для калькулятора, а то сейчас перетащена из brain_even
def brain_calc_main_logic(
    user_name: str,
    function_for_getting_answer,
    show_success_message_function,
    show_fail_message_function,
    number_of_attempts
):
    """
    Docstring for brain_calc_main_logic
    :param name: user name
    :type name: str
    :param function_for_getting_answer: function with question and answer
    :type function_for_getting_answer: function
    """
    counter = 0
    for _ in range(number_of_attempts):
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        operator = random.choice(["+", "-", "*"])
        math_expression_as_text = math_expression_to_string(x, y, operator)
        math_expression = get_math_expression(x, y, operator)
        user_answer = function_for_getting_answer(math_expression_as_text)
        correct_answer = math_expression(_)
        if is_correct_user_answer(correct_answer, user_answer):
            print("Correct!")
            counter += 1
        else:
            show_fail_message_function(user_name, user_answer, correct_answer)
            return
    show_success_message_function(user_name)


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
