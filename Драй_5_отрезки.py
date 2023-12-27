A, B = float(input("Введите число A ")), float(input("Введите число B, меньше A "))
count = 0

while A >= B:
    A -= B
    count += 1
print(f'Отрезков B в А = {count}. Остаток А = {A}')
