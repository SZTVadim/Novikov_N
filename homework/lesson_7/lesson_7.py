# Задание 1
fruits = {"яблоко", "банан"}
new_fruits = ["груша", "виноград"]
fruits.add("апельсин")
fruits.update(new_fruits)
fruits.discard("банан")
fruits.discard("киви")
# fruits.remove("киви")
removed_fruit = fruits.pop()
print(fruits)
print(removed_fruit)


# Задание 2
coordinates = (10, 20, 30, 20, 10, 20, 40)
print(coordinates[0])
print(coordinates[-1])
print(coordinates[1:4])
30 in coordinates
coordinates.index(20)
coordinates.count(20)
coordinates.count(50)
print(len(coordinates))
