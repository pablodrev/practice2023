from itertools import permutations

arr = [1, 2, 3, 4]
print("Исходный список: ", arr)
print("Перестановки: ")
perm = permutations(arr)
for i in perm:
    print(i)
