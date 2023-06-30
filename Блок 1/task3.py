numbers = [int(input("Введите число: ")) for i in range(3)]
print("Максимальное число: ", max(numbers))
print("Числа в порядке по убыванию: ", sorted(numbers, reverse=True))