# Задача 1
# Условие: Дан файл целых чисел, содержащий не менее четырёх элементов. Вывести первый, второй,
# предпоследний и последний элементы. Если чисел меньше 3 — выводить ошибку.
# Решение:
with open('numbers.txt', 'r') as f:
    numbers = [int(line.strip()) for line in f if line.strip()]

if len(numbers) < 3:
    print("Ошибка: чисел меньше 3")
else:
    # Выводим результат:
    print(f"Первый: {numbers[0]}")
    print(f"Второй: {numbers[1]}")
    print(f"Предпоследний: {numbers[-2]}")
    print(f"Последний: {numbers[-1]}")

# Пояснение:
# [int(line.strip()) for line in f if line.strip()] — list comprehension: читаем строки,
# убираем \n, преобразуем в int.
# numbers[-2] — предпоследний элемент.
# Проверка len(numbers) < 3 перед доступом.


# Задача 2
# Условие: Дан файл целых чисел. Создать два новых файла: первый — чётные, второй — нечётные
# (в том же порядке). Если чётных или нечётных нет — файл оставить пустым.
# Решение:
with open('numbers.txt', 'r') as f:
    numbers = [int(line.strip()) for line in f if line.strip()]

with open('even.txt', 'w') as f_even, open('odd.txt', 'w') as f_odd:
    for number in numbers:
        if number % 2 == 0:
            # Выводим результат:
            f_even.write(f"{number}\n")
        else:
            # Выводим результат:
            f_odd.write(f"{number}\n")

# Пояснение:
# Открываем сразу два файла через with (можно через ,).
# Проверяем чётность через number % 2 == 0.
# Если чётных нет — файл even.txt останется пустым (мы в него ничего не записали).


# Задача 3
# Условие: Дан файл вещественных чисел. Заменить в нём все элементы на их квадраты.
# Решение:
with open('numbers.txt', 'r') as f:
    numbers = [float(line.strip()) for line in f if line.strip()]

squares = [number ** 2 for number in numbers]

with open('numbers.txt', 'w') as f:
    for square in squares:
        # Выводим результат:
        f.write(f"{square}\n")

# Пояснение:
# Читаем вещественные числа (float).
# Возводим в квадрат через ** 2.
# Перезаписываем тот же файл ('w' — перезапись).


# Задача 4
# Условие: Даны два файла произвольного типа. Поменять местами их содержимое.
# Файлы должны быть бинарного типа.
# Решение:
# Читаем содержимое обоих файлов
with open('file1.bin', 'rb') as f1:
    content1 = f1.read()

with open('file2.bin', 'rb') as f2:
    content2 = f2.read()

# Записываем содержимое в обратном порядке
with open('file1.bin', 'wb') as f1:
    f1.write(content2)

with open('file2.bin', 'wb') as f2:
    f2.write(content1)

# Пояснение:
# Режим rb — чтение в бинарном виде.
# Режим wb — запись в бинарном виде.
# Читаем оба файла в память, затем записываем в противоположные.
