import random
from brain_games.cli_even import welcome_user_and_getting_name, getting_answer


def main():
    number_for_checking = random.randint(1, 100)
    name = welcome_user_and_getting_name()
    answer = getting_answer(number_for_checking)
    
    is_correct_user_answer = (number_for_checking, answer)
    
    if is_correct_user_answer:
        print("Correct!")
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{number_for_checking}'.")
        print(f"Let's try again, {name}!")

    

if __name__ == "__main__":
    main()