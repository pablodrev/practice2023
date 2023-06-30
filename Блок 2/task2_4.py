import math

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a == 0 and b == 0 and c == 0:
    print("x = любое значение")
elif a == 0 and b == 0:
    print("Нет решений.")
elif a == 0:
    x = -c/b
    print("x = ", x)
else:
    d = b**2 - 4*a*c
    if d < 0:
        print("Корней нет.")
    elif d == 0:
        x = -1*b/2*a
        print("x = ", x)
    else:
        x1 = (-1*b - math.sqrt(d))/2*a
        x2 = (-1*b + math.sqrt(d))/2*a
        print("x1 = ", x1)
        print("x2 = ", x2)
