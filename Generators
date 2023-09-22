import string
import random

def generate_password(length=8, include_uppercase=True, include_lowercase=True, include_digits=True, include_special_chars=True):
    characters = ''
    
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))

    return password

length = int(input("Enter the desired password length / Введите желаемую длину пароля: "))
print('')
include_uppercase = input("Include uppercase letters (Yes / No) / Включать ли заглавные символы (Да / Нет): ").lower() == "да"

include_lowercase = input("Include lowercase letters (Yes / No) / Включать ли строчные символы (Да / Нет): ").lower() == "да"

include_digits = input("Include digits (Yes / No) / Включать ли цифры (Да / Нет): ").lower() == "да" 

include_special_chars = input("Include special characters (Yes / No) / Включать ли специальные символы (Да / Нет): ").lower() == "да"

password = generate_password(length, include_uppercase, include_lowercase, include_digits, include_special_chars)
print("\nСгенерированный пароль / Generated password:\n", password)
