# Проверка на палиндром
def is_plalindrome(text):
    # Сравниваем первый и последний символ, потом второй и предпоследний, и т.д.
    # Если не совпадают - значит слово не палиндром
    for i in range(len(text)):
        if text[i] != text[-1 - i]:
            return False
    return True


a = input()

# Используем множество, чтобы избежать дубликтов
found = set()
# Проверяем все подстроки на наличие палиндромов
for i in range(len(a)):
    for j in range(i + 1, len(a) + 1):
        if is_plalindrome(a[i:j]):
            found.add(a[i:j])

print(found)
