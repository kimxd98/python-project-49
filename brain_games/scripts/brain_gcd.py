#!/usr/bin/env

import prompt
import random
import math
number_of_steps = 3


def show_wrong_answer(user_answer, game_answer, user_name):
    print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(
        user_answer, game_answer))
    print("Let's try again, {}!".format(user_name))


def brain_gcd():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f"Hello, {user_name}!")
    print('Find the greatest common divisor of given numbers.')
    for step in range(number_of_steps):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        game_answer = math.gcd(num1, num2)
        user_answer = prompt.string(f'Question: {num1} {num2} \nYour answer: ')
        if user_answer.isnumeric():
            if int(user_answer) != int(game_answer):
                show_wrong_answer(user_answer, game_answer, user_name)
                return
            else:
                print('Correct!')
        else:
            show_wrong_answer(user_answer, game_answer, user_name)
            return
        print('Congratulations, {}!'.format(user_name))


def main():
    brain_gcd()


if __name__ == '__main__':
    main()
