sum = 0
while (n := int(input("Введите число: "))) < 0:
    print(n)
    sum += n

print("Финальная сумма: ", sum)
