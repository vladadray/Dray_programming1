N = int(input("Введите целое число N больше нуля "))
stepen = 1
flag = False

while 3 ** stepen <= N:
    if 3 ** stepen == N:
        flag = True
        break
    stepen += 1

if flag:
    print(flag)
else:
    print(flag)

