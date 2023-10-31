# Даны N точек на прямой. У каждой известны координата X и масса M. Задача: вывести координаты точек в порядке убывания массы.
# Программа считывает натуральное число N — количество точек. Далее программа построчно считывает параметры для каждой n-ой точки: координату xi и массу mi. Оба параметра являются целыми числами, масса является положительным числом. Гарантируется, что строгого совпадения масс двух точек в считываемых данных не встречается.
# Программа должна вывести координаты xi точек, отсортированных по убыванию массы, каждая в новой строке.

N = int(input()) # Количество точек
coordinates = dict()

for i in range(N):
    x, m = map(int, input().split())
    coordinates[m] = x

masses = [*coordinates.keys()]
masses.sort(reverse=True)

for mass in masses:
    print(coordinates[mass])


# N = int(input())  # Количество точек
# coordinates = {}

# for i in range(N):
#     x, m = map(int, input().split())
#     coordinates[m] = x

# masses = sorted(coordinates.keys(), reverse=True)

# for mass in masses:
#     print(coordinates[mass])
