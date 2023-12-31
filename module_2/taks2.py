# Напишите программу для расчета времени для накопления нужной суммы на депозите. Каждый месяц проценты добавляются к сумме вклада, в следующий месяц процент рассчитывается на увеличенную в предыдущем месяце сумму вклада.
# Входными данными для программы являются три числа: начальная сумма, требуемая сумма, процентная ставка в месяц. Все три значения являются числами с плавающей точкой.
# Результатом выполнения программы будет целое число месяцев, за которое накопится требуемая сумма.

amount = float(input())
target = float(input())
rate = float(input()) / 100

months = 0

while amount < target:
    amount += amount * rate;
    months += 1

print(months)