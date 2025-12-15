import prompt


def welcome_user_and_getting_name() -> str:
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name
    


def getting_answer(number: int) -> str:
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    print(f"Question: {number}")
    return prompt.string("Your answer: ")
