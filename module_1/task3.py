# Егор разрабатывает приложение «Кошечки-собачки». Ему нужно считать данные о питомце, которые введены в консоль, и подтвердить их ввод путем вывода на экран.
# На вход программа получает четыре параметра: имя питомца (name), вид животного (animal), порода (breed) и возраст (age).
# Необходимо вывести введенную информацию в виде:
# Ваш питомец: animal name
# Порода питомца: breed
# Возраст питомца: age

name = input()
animal = input()
breed = input()
age = input()

print(f'Ваш питомец: {animal} {name}')
print(f'Порода питомца: {breed}')
print(f'Возраст питомца: {age}')