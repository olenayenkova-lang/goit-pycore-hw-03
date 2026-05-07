from datetime import datetime

def get_days_from_today(date: str) -> int:
    try:
        # Перетворюємо рядок у дату
        input_date = datetime.strptime(date, "%Y-%m-%d").date()
        
        # Поточна дата
        today = datetime.today().date()
        
        # Різниця в днях
        delta = today - input_date
        
        return delta.days
    
    except ValueError:
        raise ValueError("Неправильний формат дати. Використовуйте 'YYYY-MM-DD'")