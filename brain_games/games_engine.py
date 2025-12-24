
from brain_games.games.brain_calc_logic import brain_calc_main_logic
from brain_games.games.brain_even_logic import brain_even_main_logic
from brain_games.games.brain_gcd_logic import brain_gcd_main_logic
from brain_games.games.util_functions_for_games import (
    show_expression_to_user_and_getting_user_answer,
    show_success_message,
    show_fail_message,
    show_the_task,
    welcome_user_and_getting_user_name
)


def even_brain():
    user_name = welcome_user_and_getting_user_name()
    show_the_task("Answer 'yes' if the number is even, otherwise answer 'no'.")
    brain_even_main_logic(
        user_name,
        show_expression_to_user_and_getting_user_answer,
        show_success_message,
        show_fail_message,
        number_of_attempts=3
    )


def calc_brain():
    user_name = welcome_user_and_getting_user_name()
    show_the_task("What is the result of the expression?")
    brain_calc_main_logic(
        user_name,
        show_expression_to_user_and_getting_user_answer,
        show_success_message,
        show_fail_message,
        number_of_attempts=3
    )


def gcd_brain():
    user_name = welcome_user_and_getting_user_name()
    show_the_task("Find the greatest common divisor of given numbers.")
    brain_gcd_main_logic(
        user_name,
        show_expression_to_user_and_getting_user_answer,
        show_success_message,
        show_fail_message,
        number_of_attempts=3
    )
