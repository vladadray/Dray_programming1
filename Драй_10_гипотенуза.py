def gipotenusa():
    C = (katet1 ** 2 + katet2 ** 2) ** 0.5
    return(C)

print('Введите значение одного из катетов')
katet1 = float(input())
print(f'Введите значение другого катета')
katet2 = float(input())

print(gipotenusa())