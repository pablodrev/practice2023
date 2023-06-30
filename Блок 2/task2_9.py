number = list(map(int, input("Введите число, в котором все цифры различны: ")))

ans_1 = number.index(max(number)) + 1
ans_2 = len(number) - ans_1 + 1

print("Номер максимального числа, считая с начала: ", ans_1)
print("Номер максимального числа, считая с конца: ", ans_2)
