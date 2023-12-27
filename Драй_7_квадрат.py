A, B, C = int(input("Введите положительное число A ")), int(input("Введите положительное число B ")), int(input("Введите положительное число C "))
CvA, CvB = 0, 0
znach = 0
while A >= C:
    A -= C
    B1 = B
    while B1 >= C:
        B1 -= C
        CvB += 1
print(CvB)
