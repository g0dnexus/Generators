import random

while True:
    try:
        num = int(input("Enter the number of items / Введите количество элементов: "))
        elements = []
        for i in range(num):
            element = input(f"Enter an element / Введите элемент {i+1}: ")
            elements.append(element)

        generations = int(input("Enter the number of generations / Введите количество генераций: "))
        for _ in range(generations):
            random_element = random.choice(elements)
            print("Generated item / Сгенерированный элемент:", random_element)

        choice = input("Would you like to continue? (yes/no) / Хотите продолжить? (да/нет): ")
        while choice.lower() not in ["да", "yes", "нет", "no"]:
            print("Ошибка: некорректный ввод команды.")
            choice = input("Would you like to continue? (yes/no) / Хотите продолжить? (да/нет): ")
        
        if choice.lower() == "нет" or choice.lower() == "no":
            break

    except ValueError:
        print("Error: incorrect number entry. / Ошибка: некорректный ввод числа.")

    except Exception as e:
        print("Error / Ошибка:", str(e))
