number = int(input("Введите число: "))
even = lambda x: "Четное" if x % 2 == 0 else "Нечетное"

print(even(number))