def convert_grade(letter_grade):
    if letter_grade == "A+" or letter_grade == "A":
        return 4.0
    elif letter_grade == "A-":
        return 3.7
    elif letter_grade == "B+":
        return 3.3
    elif letter_grade == "B":
        return 3.0
    elif letter_grade == "B-":
        return 2.7
    elif letter_grade == "C+":
        return 2.3
    elif letter_grade == "C":
        return 2.0
    elif letter_grade == "C-":
        return 1.7
    elif letter_grade == "D+":
        return 1.3
    elif letter_grade == "D":
        return 1.0
    elif letter_grade == "F":
        return 0
    else:
        return "Введенное значение не является буквенной оценкой"

grade = input("Введите буквенную оценку: ")
numeric_grade = convert_grade(grade)
print(numeric_grade)