from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        # Перетворюємо рядок у дату
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # День народження у поточному році
        birthday_this_year = birthday.replace(year=today.year)

        # Якщо день народження вже минув — беремо наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Різниця між датами
        delta_days = (birthday_this_year - today).days

        # Перевіряємо, чи входить у наступні 7 днів
        if 0 <= delta_days <= 7:

            congratulation_date = birthday_this_year

            # Якщо день народження у суботу (5) або неділю (6)
            # переносимо на понеділок
            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)

            # Додаємо результат у список
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays


# Приклад використання
users = [
    {"name": "John Doe", "birthday": "1985.05.23"},
    {"name": "Jane Smith", "birthday": "1990.05.07"},
    {"name": "Alice Brown", "birthday": "1992.05.09"}
]

upcoming_birthdays = get_upcoming_birthdays(users)

print("Список привітань на цьому тижні:")
print(upcoming_birthdays)