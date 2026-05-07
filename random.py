import random

def get_numbers_ticket(min_num: int, max_num: int, quantity: int) -> list:
    # Перевірка вхідних параметрів
    if (
        min_num < 1 or
        max_num > 1000 or
        min_num > max_num or
        quantity < 1 or
        quantity > (max_num - min_num + 1)
    ):
        return []
    
    # Генерація унікальних випадкових чисел
    numbers = random.sample(range(min_num, max_num + 1), quantity)
    
    # Сортування результату
    return sorted(numbers)
