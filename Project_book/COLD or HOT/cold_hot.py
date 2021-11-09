import random

num_digits = 3
max_guess = 10


def get_secret_num():
    numbers = list(range(10))
    random.shuffle(numbers)
    secret_num = ""
    for i in range(num_digits):
        secret_num += str(numbers[i])
    return secret_num


def get_clues(guess, secret_num):
    if guess == secret_num:
        return 'Вы угадали!'

    clues = []
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append("Горячо")
        elif guess[i] in secret_num:
            clues.append("Тепло")

    if len(clues) == 0:
        return 'Холодно'

    clues.sort()
    return ' '.join(clues)


def is_only_digits(num):
    if num == '':
        return False

    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False
    return True


print('Я загадаю %s-х значное число, которое вы должны отгадать.' % num_digits)
print('Я дам несколько подсказок...')
print('Когда я говорю:  Это означает:')
print(' Холодно         Ни одна цифра не отгадана.')
print(' Тепло           Одна цифра отгадана, но не отгадана ее позиция.')
print(' Горячо          Одна цифра и ее позиция отгаданы.')

while True:
    secret_num = get_secret_num()
    print('Итак, я загадал число. У вас есть %s попыток, чтобы отгадать его.' % max_guess)

    guesses_taken = 1
    while guesses_taken <= max_guess:
        guess = ''
        while len(guess) != num_digits or not is_only_digits(guess):
            print('Попытка No%s: ' % guesses_taken)
            guess = input()

        print(get_clues(guess, secret_num))
        guesses_taken += 1

        if guess == secret_num:
            break
        if guesses_taken > max_guess:
            print('Попыток больше не осталось. Я загадал число %s.' % secret_num)

    print('Хотите сыграть еще раз? (да или нет)')
    if not input().lower().startswith('д'):
        break
