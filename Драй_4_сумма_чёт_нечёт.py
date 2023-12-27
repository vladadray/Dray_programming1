
A = int(input("Введите целое число A: ")) 
B = int(input("Введите целое число B, больше A: "))
sum = 0
sum_even = 0
sum_odd = 0

for i in range(A, B + 1):
    sum += i
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i
print(f"""Сумма чисел от {A} до {B} = {sum}
Сумма четных чисел от {A} до {B} = {sum_even}
Сумма нечетных чисел от {A} до {B} = {sum_odd}""")