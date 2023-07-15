a = int(input("Начало диапазлна: "))
b = int(input("Конец диапазона: "))

for i in range(a, b + 1):
    # Поиск делителей от 2 до корня из i
    for j in range(2, int(i ** 0.5) + 1):
        # Если найден делитель, то число не простое
        if i % j == 0:
            break
    else:
        print(i)
