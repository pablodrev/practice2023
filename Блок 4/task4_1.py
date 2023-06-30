number = input("Введите число: ")
biggest = int("".join(sorted(number, reverse=True)))
print(biggest)