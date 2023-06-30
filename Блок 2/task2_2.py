def print_programs(programs):
    print("Программы: ")
    for p in programs:
        print(p)


tv_programs = ["Новости", "Фильмы", "Музыка", "Спорт"]
print_programs(tv_programs)

new_program = input("Введите название новой программы: ")
position = int(input("Введите номер позиции: "))

tv_programs.insert(position-1, new_program)
print_programs(tv_programs)
