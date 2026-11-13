# Задание 1
# Пункт 1
def calculate_total(price, tax_percent):
    if tax_percent > 20 or price < 0:
        return "Ошибка"

    tax = price * tax_percent / 100
    total = price + tax

    return total


# Пункт 2
def get_level(points):
    if points >= 100:
        return "Эксперт"
    elif points >= 50:
        return "Продвинутый"
    elif points >= 20:
        return "Начинающий"
    else:
        return "Новичок"


# Задание 2
def process_status(status):
    match status:
        case "active":
            return "Статус активен"
        case "inactive":
            return "Статус неактивен"
        case "pending":
            return "Статус в ожидании"
        case "blocked":
            return "Статус заблокирован"
        case _:
            return "Неизвестный статус"
