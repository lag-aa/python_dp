# Double print

# Напишите функцию double_print, которая принимает строку и выводит ее на экран дважды.

# При передачи пустой строки, функция должна возбудить исключение ValueError с сообщением "empty string is not allowed"

# Пример работы программы:

# >>> double_print('Hello')
# Hello
# Hello

# >>> double_print('')
# Traceback (most recent call last):
#   ...
# ValueError: empty string is not allowed


def double_print(text):
    if len(text) == 0:
        raise ValueError("empty string is not allowed")

    print(text)
    print(text)

# double_print('')