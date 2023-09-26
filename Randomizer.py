import random
from collections import Counter

def generate_random_numbers():
    num1 = int(input("Enter the first number / Введите первое число: "))
    num2 = int(input("Enter the second number / Введите второе число: "))

    while num2 <= num1:
        print("The second number must be greater than the first. Try again. / Второе число должно быть больше первого. Попробуйте еще раз.")
        num2 = int(input("Enter the second number / Введите второе число: "))

    count = int(input("Enter the number of random numbers to generate / Введите количество случайных чисел для генерации: "))
    if count <= 0:
        print("The number of random numbers must be greater than 0. Try again. / Количество случайных чисел должно быть больше 0. Попробуйте еще раз.")
        return

    random_numbers = []
    for _ in range(count):
        random_number = random.randint(num1, num2)
        random_numbers.append(random_number)

    print("Generated random numbers / Сгенерированные числа:")
    for number in random_numbers:
        print(number)
    
    number_counts = Counter(random_numbers)
    most_common = number_counts.most_common(3)
    
    print("\nMost common numbers / Самые частые числа:")
    for number, count in most_common:
        print(f"Number: {number}, Count: {count}")
    
 
    least_common = number_counts.most_common()[:-4:-1]
    print("\nLeast common numbers / Самые нечастые числа:")
    for number, count in least_common:
        print(f"Number: {number}, Count: {count}")

generate_random_numbers()
