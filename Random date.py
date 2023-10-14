import random
from datetime import datetime, timedelta

def validate_date(date_string):
    try:
        datetime.strptime(date_string, "%d.%m.%Y")
        return True
    except ValueError:
        return False

def generate_random_date(start_date, end_date):
    start_date_dt = datetime.strptime(start_date, "%d.%m.%Y")
    end_date_dt = datetime.strptime(end_date, "%d.%m.%Y")
    
    if start_date_dt > end_date_dt:
        raise ValueError("The start date cannot be greater than the end date / Начальная дата не может быть больше конечной даты.")
    
    delta = (end_date_dt - start_date_dt).days
    random_days = random.randint(0, delta)
    random_date = start_date_dt + timedelta(days=random_days)
    
    return random_date.strftime("%d.%m.%Y")

def main():
    while True:
        start_date_input = input("Enter the start date (DD.MM.YYYY) / Введите начальную дату (ДД.ММ.ГГГГ): ")
        end_date_input = input("Enter the end date (DD.MM.YYYY) / Введите конечную дату (ДД.ММ.ГГГГ): ")
        
        if not validate_date(start_date_input) or not validate_date(end_date_input):
            print("Incorrect date format. Enter the date in DD.MM.YYYY format / Неправильный формат даты. Введите дату в формате ДД.ММ.ГГГГ.")
            continue

        try:
            random_date = generate_random_date(start_date_input, end_date_input)
            print(f"Random date: {random_date} / Случайная дата: {random_date}")
        except ValueError as e:
            print(str(e))
        
        choice = input("Do you want to continue? (y/n) / Хотите продолжить? (д/н): ")
        while choice.lower() not in ["y", "n", "д", "н"]:
            print("Incorrect choice. Enter 'y' for yes or 'n' for no / Неправильный выбор. Введите 'д' для да или 'н' для нет")
            choice = input("Do you want to continue? (y/n) / Хотите продолжить? (д/н): ")
        
        if choice.lower() == "n" or choice.lower() == "н":
            break

if __name__ == "__main__":
    main()
