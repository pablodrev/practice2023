score = int(input("Кол-во очков: "))
if score == 3:
    print("Выигрыш")
elif score == 0:
    print("Проигрыш")
elif score == 1:
    print("Ничья")
else:
    print("Неверный ввод")