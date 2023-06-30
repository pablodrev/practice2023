def not_prime(x):
    if x <= 1:
        return True
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return True
    return False


n = int(input("Введите число N: "))
arr = [i for i in range(n) if not_prime(i)]
print("Не простые числа от 0 до N", arr)
