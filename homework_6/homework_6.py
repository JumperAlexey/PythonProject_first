# Задача 1
# Условие: Дан список результатов автотестов со статусами PASS, FAIL, SKIP. Напишите рекурсивную функцию,
# которая подсчитывает количество тестов со статусом PASS. Использовать циклы for и while нельзя.
# Решение:
def count_pass(results):
    if not results:  # базовый случай: пустой список
        return 0
    # рекурсивный вызов: проверяем первый элемент + обрабатываем остаток
    return (1 if results[0] == "PASS" else 0) + count_pass(results[1:])


tests = ["PASS", "FAIL", "PASS", "SKIP", "PASS"]
# Выводим результат:
print(count_pass(tests))  # 3

# Пояснение:
# Базовый случай: пустой список → 0.
# Рекурсивный вызов: проверяем первый элемент, добавляем к результату подсчёта оставшихся.
# results[1:] — срез без первого элемента.


# Задача 2
# Условие: Напишите функцию create_time_checker(max_time), которая возвращает вложенную функцию для проверки
# времени выполнения теста. Вложенная функция принимает фактическое время выполнения и сообщает, превышен
# лимит или нет. Создайте два независимых замыкания с разными max_time и продемонстрируйте их работу.
# Решение:
def create_time_checker(max_time):
    def check(actual_time):
        if actual_time > max_time:
            return f"Превышен лимит ({actual_time} > {max_time})"
        return f"В пределах нормы ({actual_time} <= {max_time})"
    return check


check_1s = create_time_checker(1.0)
check_5s = create_time_checker(5.0)

# Выводим результат:
print(check_1s(0.5))   # В пределах нормы (0.5 <= 1.0)
print(check_1s(1.5))   # Превышен лимит (1.5 > 1.0)
print(check_5s(3.0))   # В пределах нормы (3.0 <= 5.0)
print(check_5s(7.0))   # Превышен лимит (7.0 > 5.0)

# Пояснение:
# create_time_checker(max_time) возвращает замыкание check.
# Каждый вызов создаёт независимое замыкание с сохранённым max_time.
# Внутренняя функция использует max_time из внешней (enclosing scope).


# Задача 3
# Условие: Напишите декоратор log_test, который перед запуском тестовой функции выводит её имя, после
# выполнения сообщает о завершении и выводит полученный результат. Декоратор должен поддерживать функции
# с произвольным количеством позиционных и именованных аргументов через *args и **kwargs. Используйте functools.wraps().
# Решение:
from functools import wraps


def log_test(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Запуск теста: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Тест завершён: {func.__name__}")
        print(f"Результат: {result}")
        return result
    return wrapper


@log_test
def test_login(username, password, remember=False):
    return f"Успешный вход: {username}, remember={remember}"


@log_test
def test_sum(a, b):
    return a + b


# Выводим результат:
test_login("admin", "secret", remember=True)
test_sum(2, 3)

# Пояснение:
# @wraps(func) сохраняет имя и docstring исходной функции.
# *args, **kwargs — для работы с любыми аргументами.
# Возвращаем результат через return result.


# Задача 4
# Условие: Напишите декоратор с параметром retry(count), который повторно запускает декорируемую функцию
# указанное количество раз, пока функция не вернёт True. Перед каждой попыткой выводится её номер. Если функция
# вернула True — дальнейшие попытки не выполняются. Декоратор поддерживает *args и **kwargs.
# Решение:
from functools import wraps


def retry(count):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, count + 1):
                print(f"Попытка {attempt} из {count}")
                result = func(*args, **kwargs)
                if result is True:
                    print(f"Успех на попытке {attempt}")
                    return True
            print(f"Все {count} попыток завершились неудачей")
            return False
        return wrapper
    return decorator


@retry(3)
def flaky_test(attempts_until_success=2):
    # эмуляция "нестабильного" теста: успех на 2-й попытке
    if not hasattr(flaky_test, "counter"):
        flaky_test.counter = 0
    flaky_test.counter += 1
    return flaky_test.counter >= attempts_until_success


# Выводим результат:
print(flaky_test())

# Пояснение:
# retry(count) — декоратор с параметром (три уровня вложенности).
# Цикл for attempt in range(1, count + 1) выполняет попытки.
# Если функция вернула True — выходим из цикла (return True).
# Если все попытки провалились — возвращаем False.
# @wraps(func) сохраняет метаданные.
