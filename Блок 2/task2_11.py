a = int(input("a = "))
b = int(input("b = "))

sum = 0

if a < b:
    for i in range(a, b+1):
        sum += i
elif a > b:
    for i in range(b, a+1):
        sum += i

print("Сумма от a до b =", sum)
