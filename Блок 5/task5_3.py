import csv


year_start = int(input("Введите начальный год: "))
year_end = int(input("Введите конечный год: "))
# Проверка на правильность введенный значений
if year_end < year_start:
    print("Конечный год должен быть больше начального!")
    exit()
filename = "prog_books.csv"

with open(filename, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    # Для каждой записи проверяем,
    # находится ли год выпуска в промежутке от начального до конечного года
    found = False
    for row in reader:
        year = int(row["Год выпуска"])
        if year_start <= year <= year_end:
            found = True
            print(row["Книга"], row["Год выпуска"], sep=", ")
    if not found:
        print("Книги за указанный период не найдены.")
