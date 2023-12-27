n = int(input("Введите целое число"))

def check_na_prostotu(chislo):
    count = 0
    flag = True
    for i in range(1, chislo + 1):
        if chislo % i == 0:
            count += 1
        if count > 2:
            flag = False
            break
    return (flag)

if __name__ == "__main__":

    Global_flag = check_na_prostotu(n)
    if Global_flag:
        print("Это простое число")
    else:
        print("Это не простое число")