# Python часто используют для решения математических задач, одна из них — вычисление суммы ряда. Напишите программу, 
# которая будет вычислять и выводить на экран целое число — сумму квадратов натуральных чисел до N, где N — натуральное число 
# (N>1), подаваемое на вход программы.
# 1+2^2+3^2+...+N^2
N = int(input())
sum = 0;

for i in range(1, N + 1):
    sum += i**2

print(sum)