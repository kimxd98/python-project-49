#!/usr/bin/env

import prompt
import random
number_of_steps = 3


def brain_even():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f"Hello, {user_name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for step in range(number_of_steps):
        num = random.randint(1, 20)
        if num % 2 == 0:
            game_answer = 'yes'
        else:
            game_answer = 'no'
        user_answer = prompt.string(f'Question: {num} \nYour answer: ')
        if user_answer != game_answer:
            print("'{}' is wrong answer ;(. Correct answer was '{}'."
                  .format(user_answer, game_answer))
            print("Let's try again, {}!".format(user_name))
            return
        else:
            print('Correct!')
    print('Congratulations, {}!'.format(user_name))


def main():
    brain_even()


if __name__ == '__main__':
    main()
