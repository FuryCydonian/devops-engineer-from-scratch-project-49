import prompt


def welcome_user_and_getting_user_name() -> str:
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def show_expression_to_user_and_getting_user_answer(question_expression) -> str:
    print(f"Question: {question_expression}")
    return prompt.string("Your answer: ")


def show_the_task(task: str):
    print(task)


def show_fail_message(user_name, user_answer, correct_answer) -> None:
    print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
    print(f"Let's try again, {user_name}!")


def is_correct_user_answer(correct_answer, user_answer) -> bool:
    return str(correct_answer) == str(user_answer)


def show_success_message(user_name: str) -> None:
    print(f"Congratulations, {user_name}!")
