import csv  # Библиотека для работы с .csv


# Добавляет строку в .csv файл
def csv_add_row(filename, row):
    with open(filename, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(row)


filename = "prog_books.csv"

# Добавление записей
n_rows = int(input("Сколько записей вы ходите добавить?: "))
for i in range(n_rows):
    print(f"Добавление записи {i+1}")
    book = input("Введите название книги: ")
    author = input("Введите автора: ")
    year = input("Введите год выпуска: ")
    row = [book, author, year]
    csv_add_row(filename, row)
    print("Запись добавлена.\n")

# Поиск книги по автору
name = input("Введите автора для поиска его книг: ")
with open(filename, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    # Для каждой строки в файле проверяем,
    # содержит ли столбец "Автор" искомое значение
    found = False
    for row in reader:
        if name in row["Автор"]:
            found = True
            print(row["Книга"], row["Автор"], sep=", ")
    if not found:
        print("Книги не найдены.")
