import random

hangman_pic = ["""
+---+
    |
    |
    |
   ===""", """
+---+
 O  |
 |  |
    |
   ===""", """
+---+
 O  |
/|  |
    |
   ===""", """
+---+
 O  |
/|\ |
    |
   ===""", """
+---+
 O  |
/|\ |
/   |
   ===""", """
+---+
 O  |
/|\ |
/ \ |
   ===""", """
+---+
[O  |
/|\ |
/ \ |   
   """, """
+---+
[O] |
/|\ |
/ \ |
   """]

words = {'Цвета': 'красный оранжевый желтый зеленый синий голубой фиолетовый белый черный коричневый'.split(),

         'Фигуры': 'квадрат треугольник прямоугольник круг эллипс ромб трапеция параллелограмм пятиугольник '
                   'шестиугольник восьмиугольник'.split(),

         'Фрукты': 'яблоко апельсин лимон лайм груша мандарин виноград грейпфрут персик банан абрикос манго банан '
                   'нектарин'.split(),

         'Животные': 'аист бабуин баран барсук бык волк зебра кит коза корова кошка кролик крыса лев лиса лось '
                     'медведь мул мышь норка носорог обезьяна овца олень осел панда пума скунс собака сова тигр '
                     'тюлень хорек ящерица'.split()}


def get_random_word(word_dict):
    word_key = random.choice(list(word_dict.keys()))
    word_index = random.randint(0, len(word_dict[word_key]) - 1)
    return [word_dict[word_key][word_index], word_key]


def display_board(missed_letters, correct_letters, secret_word):
    print(hangman_pic[len(missed_letters)])
    print()

    print("Неверные буквы:", end='')
    for letter in missed_letters:
        print(letter, end='')
    print()

    blanks = '_' * len(secret_word)

    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i + 1:]

    for letter in blanks:
        print(letter, end='')
    print()


def get_guess(already_guess):
    while True:
        print("Введите букву.")
        guess = input().lower()

        if len(guess) != 1:
            print("Пожалуйста, введите одну букву.")
        elif guess in already_guess:
            print("Эта буква уже была")
        elif guess not in 'абвгдеежзийклмнопрстуфхцчшщъыьэюя':
            print("Введите БУКВУ!")
        else:
            return guess


def play_again():
    print("Хотите сыграть еще? (Д/Н)")
    return input().lower().startswith('д')


print("В И С Е Л И Ц А")

difficulty = ''
while difficulty not in 'лст':
    print('Выберите уровень сложности: Л - Легкий, С - Средний, Т - Тяжелый')
    difficulty = input().lower()
if difficulty == 'c':
    del hangman_pic[8]
    del hangman_pic[7]
if difficulty == 'т':
    del hangman_pic[8]
    del hangman_pic[7]
    del hangman_pic[5]
    del hangman_pic[3]

missed_letters = ''
correct_letters = ''
secret_word, secret_set = get_random_word(words)
game_is_done = False

while True:
    print('Секретное слово из набора: ' + secret_set)
    display_board(missed_letters, correct_letters, secret_word)

    guess = get_guess(missed_letters + correct_letters)

    if guess in secret_word:
        correct_letters = correct_letters + guess

        found_all_letters = True
        for i in range(len(secret_word)):
            if secret_word[i] not in correct_letters:
                found_all_letters = False
                break
        if found_all_letters:
            print("ДА! Секретное слово - " + secret_word + "! Вы угадали!")
            game_is_done = True
    else:
        missed_letters = missed_letters + guess

        if len(missed_letters) == len(hangman_pic) - 1:
            display_board(missed_letters, correct_letters, secret_word)
            print("У вас закончились догадки!\nПосле " + str(len(missed_letters)) + ' упущенные догадки и '
                  + str(len(correct_letters)) + " правильные догадки, слово было " + secret_word + "'")
            game_is_done = True

    if game_is_done:
        if play_again():
            missed_letters = ''
            correct_letters = ''
            game_is_done = False
            secret_word, secret_set = get_random_word(words)
        else:
            break
