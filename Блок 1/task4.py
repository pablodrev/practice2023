while True:
    number = int(input("Введите число от 10 до 20: "))
    if number < 10:
        print("Число меньше требуемого диапазона, повторите попытку.")
        continue
    elif number > 20:
        print("Число больше требуемого диапазона, повторите попытку.")
        continue
    else:
        print("Спасибо")
        break
