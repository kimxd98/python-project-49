import prompt


def welcome():
    print('Welcome to the Brain Games!')

def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

def main():
    welcome()
    welcome_user()

if __name__ == '__main__':
    main()
