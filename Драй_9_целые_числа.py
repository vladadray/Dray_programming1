def converter(number):
    sp = ['Один', 'Два', 'Три', 'Четыре', 'Пять', 'Шесть',
          'Семь', 'Восемь', 'Девять', 'Десять', 'Одиннадцать', 'Двенадцать']
    return (sp[number])

if __name__ == "__main__":
    converter(0)
    for i in range(12):
        print(i + 1, '=', converter(i))