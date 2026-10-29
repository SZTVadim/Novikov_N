# Задание 1
fruits = ["яблоко"]
fruits.append("банан")
fruits.extend(["апельсин", "груша"])
fruits.insert(1, "виноград")


# Задание 2
fruits = ["яблоко", "банан", "апельсин", "банан"]
fruits.remove("банан")
new_fruits = fruits.pop()


# Задание 3
fruits = ["яблоко", "банан", "апельсин", "банан"]
fruits.index("банан")
fruits.count("банан")


# Задание 4
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()
numbers.reverse()
print(numbers)


# Задание 5
cube = [n ** 3 for n in range(1, 9)]
print(min(cube))
print(max(cube))


# Задание 6
roster = [5, 12, 8, 15, 3, 20, 7, 18, 9, 11]
ten_roster = [number for number in roster if number > 10]
print(sum(ten_roster))


# Задание 7
cities = ["москва", "санкт-петербург", "казань"]
title_cities = [city.title() for city in cities]
print(title_cities)
