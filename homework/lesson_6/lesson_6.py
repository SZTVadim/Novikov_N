# Задание 1
student_info = {
    "имя": "Иван",
    "возраст": 20,
    "курс": 2,
    "город": "Москва"
}
print(student_info.keys())
print(student_info.values())
for key, value in student_info.items():
    print(f"Ключ: {key}, Значение: {value}")
for value in student_info.values():
    print(value)


# Задание 2
prices = {"яблоко": 50, "банан": 30, "апельсин": 40, "груша": 35, "виноград": 60}
del prices["груша"]
removed_price = prices.pop("виноград")
discounted_prices = {
    fruit: price * 0.9
    for fruit, price in prices.items()
}
print(discounted_prices)


# Задание 3
student1 = {"имя": "Иван", "возраст": 20, "курс": 2}
student2 = {"имя": "Мария", "возраст": 21, "город": "Санкт-Петербург"}
original_student1 = student1.copy()
student1.update(student2)
print(student1)
student3 = original_student1.copy()
student3.update(student2)
print(original_student1)
print(student2)
print(student3)
