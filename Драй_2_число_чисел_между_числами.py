A, B = int(input("Введите число A ")), int(input("Введите число B, больше A "))
count = 0

if A > B:
    print("А должно быть меньше B. Введите снова.")
    A, B = int(input("Введите число A ")), int(input("Введите число B, больше A "))
else:
    for i in range(A, B + 1):
        print(i, end=" ")
        count += 1
    print()
    print(f'Между числами {A} и {B} расположено {count - 2} чисел')