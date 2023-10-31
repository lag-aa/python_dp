# Напишите функцию fibonacci(index), которая находит число Фибоначчи с нужным номером. Аргумент функции index — целое положительное число.
# Последовательность Фибоначчи задается формулой:
# F(1) = 0
# F(2) = 1
# F(N) = F(N - 1) + F(N - 2) для N >= 3
# То есть, каждое последующее число равно сумме двух предыдущих чисел. Если требуется больше информации о данной последовательности, вы можете обратиться, например, к источнику.

def fibonacci(index):
    if abs(index) < 3:
        return abs(index - 1)
    elif index > 0:
        return fibonacci(index - 1) + fibonacci(index - 2)
    else:
        return fibonacci(index + 2) - fibonacci(index + 1)

number = int(input("Число: "))
print(fibonacci(number))