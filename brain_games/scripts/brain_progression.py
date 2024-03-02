#!/usr/bin/env

import prompt
import random
number_of_steps = 3


progression_limits_min = 1
progression_limits_max = 50

progression_step_min = 2
progression_step_max = 30

progression_length_min = 5
progression_length_max = 10


def show_wrong_answer(user_answer, game_answer, user_name):
    print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(
        user_answer, game_answer))
    print("Let's try again, {}!".format(user_name))


def brain_generate_progression():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f"Hello, {user_name}!")
    print('What number is missing in the progression?')
    for step in range(number_of_steps):

        start_value = random.randint(
            progression_limits_min, progression_limits_max)
        start_length = random.randint(
            progression_length_min, progression_length_max)
        start_step = random.randint(
            progression_step_min, progression_step_max)

        progression = []
        progression_max_value = start_value + (start_length * start_step)

        for i in range(start_value, progression_max_value, start_step):
            progression.append(str(i))

        index_skip_number = random.randint(0, start_length - 1)
        target_to_skip = progression[index_skip_number]
        progression[index_skip_number] = '..'
        progression = ' '.join(progression)
        game_answer = target_to_skip
        user_answer = prompt.string(f'Question: {progression} \nYour answer: ')
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
    brain_generate_progression()


if __name__ == '__main__':
    main()
