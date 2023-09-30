import random
from collections import Counter

def generate_random_letter(language_choice):
    language = language_choice.lower()
    if language == 'русский' or language == 'russian':
        letter = chr(random.randint(1040, 1071))
    elif language == 'english' or language == 'английский':
        letter = chr(random.randint(65, 90))
    else:
        return 'Выбран неверный язык'

    return letter

language_choice = input('Enter the language (Russian or English) / Введите язык (русский или английский): ')
n_generations = int(input('Enter the number of generations / Введите количество генераций: '))

letters = []
while True:
    for _ in range(n_generations):
        random_letter = generate_random_letter(language_choice)
        if random_letter != 'Выбран неверный язык':
            letters.append(random_letter)
        else:
            print(random_letter)
            exit()

    letter_counts = Counter(letters)
    most_common_letter, most_common_count = letter_counts.most_common(1)[0]

    print('Сгенерировано', n_generations, 'букв.')
    print('List of generated letters / Список сгенерированных букв:', letters)
    print('The most frequent letter / Самая частая буква:', most_common_letter)
    print('Number of generations / Количество генераций:', most_common_count)

    choice = input('Do you want to generate more letters? (yes/no) / Хотите сгенерировать еще буквы? (да/нет): ')
    if choice.lower() == 'no' or choice.lower() == 'нет':
        break

    n_generations = int(input('Enter the number of additional generations / Введите количество дополнительных генераций: '))

