# Задание№1. 6. Работа с динамической памятью
# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах.
# в первых рамках трех уроков. Проанализировать результат и определить программу с наиболее эффективным эффективным способом.
# использование памяти.
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной одной
# и той же задачи. Результаты анализа вставьте в виде комментариев к коду. Также укажите в
# комментарийх версии Python и разрядность вашей ОС.

от  pympler  импорта  трекера

# ПРИМЕР№1 В диапазоне натуральных чисел от 2 до 99 определить, сколько из них
# # кратны каждому из чисел в диапазоне от 2 до 9

# tr = tracker.SummaryTracker ()
# результат = {}
# для n в диапазоне (2, 10):
# результат [n] = []
# для f в диапазоне (2, 100):
# если f% n == 0:
# result [n] .append (f)
# print (f'Для числа {n} кратны - {len (result [n])}. Краткие числа: {result [n]}. ')
#
# Распечатать()
# tr.print_diff ()

# Результат примера №1:
# Для числа 2 кратны - 49. Краткие числа: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98].
# Для числа 3 кратны - 33. Краткие числа: [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99].
# Для числа 4 кратны - 24. Краткие числа: [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96].
# Для числа 5 кратны - 19. Краткие числа: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95] .
# Для числа 6 кратны - 16. Краткие числа: [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96].
# Для числа 7 кратны - 14. Краткие числа: [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98].
# Для числа 8 кратны - 12. Краткие числа: [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96].
# Для числа 9 кратны - 11. Краткие числа: [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99].

# типы | # объектов | общий размер
# ======================= | =========== | ============
# список | 2421 | 211,06 КБ
# str | 2411 | 165,99 КБ
# int | 421 | 11,51 КБ
# dict | 4 | 1,02 КБ
# код | 1 | 246 млрд
# кортеж | 4 | 224 млрд
# функция (store_info) | 1 | 136 млрд
# ячейка | 2 | 80 млрд
# метод | 1 | 64 млрд

# Вывод примера №1: основная память занята под сохранение получившихся чисел в виде списков (список 211.06 КБ) и вывод их в виде строк (str 165.99 КБ)

# ПРИМЕР№2 Найти сумму и произведение цифр трехного числа, который вводит пользователь
# tr = tracker.SummaryTracker ()
# n = int (input ("Введите трехзначное число:"))
#
# если 99 <n <999:
# a = n% 10
# n = n // 10
# c = n% 10
# n = n // 10
# sum_number = int (a + c + n)
# умножение = int (a * c * n)
# print (f'Сумма цифр введенного числа равно: {sum_number} ')
# print (f'Произведение цифр введенного числа равно: {multiplication} ')
# еще:
# print ("Ввведенное число не трехзначное")
# tr.print_diff ()

# результат примера №2
# Введите трехзначное число: 698
# Сумма цифр введенного числа равно: 23
# Произведение цифр введенного числа равно: 432
# типы | # объектов | общий размер
# ======================= | =========== | ============
# список | 2378 | 206,27 КБ
# str | 2376 | 163,97 КБ
# int | 421 | 11,51 КБ
# dict | 3 | 680 млрд
# функция (store_info) | 1 | 136 млрд
# ячейка | 2 | 80 млрд
# код | 0 | 70 млрд
# кортеж | 2 | 64 млрд
# метод | 1 | 64 млрд
# Вывод примера №2: основная память занята сохранение получившихся чисел в виде списков (список 206,27 КБ) и вывод их в виде строк (str 163.97)

# ПРИМЕР№3
 случайный импорт

tr  =  трекер . SummaryTracker ()
массив  = [ случайный . randint ( 1 , 10 ) для  _  в  диапазоне ( 20 )]
print ( f'Созданный массив: { array } ' )

max_index  =  0
list_number  = []
# находим максимальный кол-во повторений
для  я  в  массиве :
    если  массив . count ( i ) >  массив . количество ( max_index ):
        max_index  =  массив . счет ( я )
# находим все числа с макимальным повторением
для  я  в  массиве :
    если  массив . count ( i ) ==  max_index :
        list_number . добавить ( я )
set_number  =  набор ( список_номер )
print ( f'Максимальное число повторений равно: { max_index } для чисел: { set_number } ' )
тр . print_diff ()

# результат примера №3
# Созданный массив: [1, 1, 8, 1, 2, 3, 7, 7, 6, 9, 6, 1, 10, 6, 3, 7, 3, 8, 4, 9]
# Максимальное число повторений равно: 3 для чисел: {3, 6, 7}
# типы | # объектов | общий размер
# ======================= | =========== | ============
# список | 2380 | 206,70 КБ
# str | 2375 | 163,92 КБ
# int | 420 | 11,48 КБ
# dict | 3 | 400 млрд
# набор | 1 | 216 млрд
# функция (store_info) | 1 | 136 млрд
# ячейка | 2 | 80 млрд
# код | 0 | 70 млрд
# метод | 1 | 64 млрд
# кортеж | 1 | 8 млрд

# Проверка версии Python
import  sys

печать ( SYS . версия )
# результат: 3.8.6 (теги / v3.8.6: db45529, 23 сентября 2020 г., 15:52:53) [MSC v.1927 64 бит (AMD64)]