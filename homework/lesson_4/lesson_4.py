# Задание 1
first_string = "Привет"
first_int = 42
first_float = 3.14
first_list = [1, 2, 3]
print(
    type(first_string),
    type(first_int),
    type(first_float),
    type(first_list),
)


# Задание 2
second_string = "python PROGRAMMING"
second_string.lower()
second_string.upper()
second_string.capitalize()
second_string.title()


# Задание 3
incorrect_string = "  Hello World  "
incorrect_string.strip()
incorrect_string.lstrip()
incorrect_string.rstrip()


# Задание 4
fruit_string = "яблоко,банан,апельсин,груша"
splitted_string = fruit_string.split(",")
fruit_string = " | ".join(splitted_string)


# Задание 5
text = "Я изучаю Python. Python - это круто!"
new_text = text.replace("Python", "Java")


# Задание 6
sixth_string = "Python программирование на Python"
sixth_string.index("Python")
sixth_string.count("Python")
sixth_string.find("Java")


# Задание 7
"Hello123".isalnum()
"12345".isdigit()
"Hello".isalpha()
"   ".isspace()


# Задание 8
seventh_string = "Python very good"
print(seventh_string[:3])
print(seventh_string[-3:])
print(seventh_string[::2])
print(seventh_string[::-1])


# Задание 9
print("Он сказал: \"Привет\"")
print("Первая строка\nВторая строка")
