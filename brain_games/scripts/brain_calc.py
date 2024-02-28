import prompt
import random
number_of_steps = 3
operators = ["+","-","*"]


def brain_calc():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f"Hello, {user_name}!")
    print('What is the result of the expression?')
    for step in range(number_of_steps):
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        operator = random.choice(operators)
        game_answer = eval(str(num1)+operator+str(num2)) 
        user_answer = prompt.string(f'Question: {num1} {operator} {num2} \nYour answer: ')
        if int(user_answer) != int(game_answer):
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(
              user_answer, game_answer))
            print("Let's try again, {}!".format(user_name))
            return
        else:
            print('Correct!')
    print('Congratulations, {}!'.format(user_name))


def main():
    brain_calc()


if __name__ == '__main__':
    main()
