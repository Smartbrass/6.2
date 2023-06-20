X = int(input("Введите натуральное число:"))
count = 0
for i in range(1, X + 1):
    if X % i == 0:
        count += 1
print("Число", X, "имеет", count, "натуральных делителя/ей")


