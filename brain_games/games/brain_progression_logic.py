import random
from brain_games.games.util_functions_for_games import is_correct_user_answer


def brain_progression_main_logic(
    user_name: str,
    function_for_show_user_expression_and_getting_user_answer,
    show_success_message_function,
    show_fail_message_function,
    number_of_attempts
):
    counter = 0
    for _ in range(number_of_attempts):
        progression = get_progression()
        correct_answer = random.choice(progression)
        user_answer = function_for_show_user_expression_and_getting_user_answer(progression_to_string(progression, correct_answer))

        if is_correct_user_answer(correct_answer, user_answer):
            print("Correct!")
            counter += 1
        else:
            show_fail_message_function(user_name, user_answer, correct_answer)
            return
    show_success_message_function(user_name)


def get_progression() -> list:
    progression = []
    start = random.randint(1, 10)
    step = random.randint(1, 5)
    for index in range(10):
        current_element = start + index * step
        progression.append(current_element)
    return progression


def progression_to_string(progression: list, correct_answer: int) -> str:
    replaced = [".." if x == correct_answer else str(x) for x in progression]
    return " ".join(replaced)
