# Программа считывает натуральное число. 
# По данному натуральному числу найдите минимальное натуральное число, состоящее из тех же цифр, 
# что и данное, и выведите его на экран.
# Важно! Число не может начинаться с 0.

num = list(input())
num.sort()

if '0' in num:
    i = len([index for index, item in enumerate(num) if item == '0'])
    num[0], num[i] = num[i], num[0]

result = "".join(num)
print(result)
