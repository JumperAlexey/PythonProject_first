# Задача 1
# Условие: Дан список результатов автотестов. Для каждого теста известны название, статус (PASS, FAIL, SKIP) и
# время выполнения. С помощью filter() получить все упавшие тесты, с помощью map() — список их названий, с
# помощью reduce() — общее время выполнения всех тестов. Дополнительно через генератор списка сформировать
# список названий успешно пройденных тестов. Вывести количество тестов каждого статуса, список названий упавших
# тестов, список успешных тестов и общее время.
# Решение:
from functools import reduce

tests = [
    {"name": "test_login", "status": "PASS", "duration": 2.5},
    {"name": "test_checkout", "status": "FAIL", "duration": 5.1},
    {"name": "test_profile", "status": "PASS", "duration": 1.8},
    {"name": "test_payment", "status": "FAIL", "duration": 4.2},
    {"name": "test_search", "status": "SKIP", "duration": 0.0},
]

# Список упавших тестов через filter()
failed_tests = list(filter(lambda t: t["status"] == "FAIL", tests))

# Список их названий через map()
failed_names = list(map(lambda t: t["name"], failed_tests))

# Общее время через reduce()
total_duration = reduce(lambda acc, t: acc + t["duration"], tests, 0)

# Успешные тесты через генератор списка
passed_names = [t["name"] for t in tests if t["status"] == "PASS"]

# Подсчёт по статусам
status_counts = {
    "PASS": len([t for t in tests if t["status"] == "PASS"]),
    "FAIL": len([t for t in tests if t["status"] == "FAIL"]),
    "SKIP": len([t for t in tests if t["status"] == "SKIP"]),
}

# Выводим результат:
print(f"Всего тестов: {len(tests)}")
print(f"PASS: {status_counts['PASS']}")
print(f"FAIL: {status_counts['FAIL']}")
print(f"SKIP: {status_counts['SKIP']}")
print(f"Упавшие тесты: {failed_names}")
print(f"Успешные тесты: {passed_names}")
print(f"Общее время: {total_duration:.1f}")

# Пояснение:
# filter() отбирает тесты со статусом FAIL.
# map() извлекает только названия.
# reduce() суммирует duration (начальное значение 0).
# Генератор списка формирует passed_names.


# Задача 2
# Условие: Создать JSON-файл с тестовыми пользователями. Для каждого — логин, пароль, ожидаемый результат
# авторизации. Написать программу, которая открывает JSON, загружает данные и выводит информацию о каждом
# пользователе. Обработать ситуации: файл не существует, некорректный JSON, отсутствие обязательного поля.
# Использовать try/except с as e.
# Решение:
import json


def load_users(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError as e:
        print(f"Файл не найден: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Ошибка чтения JSON: {e}")
        return None

    try:
        users = data["users"]
    except KeyError as e:
        print(f"Отсутствует обязательное поле: {e}")
        return None

    return users


users = load_users("users.json")

if users:
    for user in users:
        try:
            login: object = user["login"]
            password = user["password"]
            expected = user["expected"]
            # Выводим результат:
            print(f"Логин: {login}, Пароль: {password}, Ожидаемо: {expected}")
        except KeyError as e:
            print(f"У пользователя {login} отсутствует поле: {e}")

# Пояснение:
# FileNotFoundError — файла нет.
# json.JSONDecodeError — файл не является валидным JSON.
# KeyError — отсутствует ключ.
# Каждая ошибка обрабатывается отдельно.


# Задача 3
# Условие: Функция принимает количество повторных запусков теста (0–5) и значение таймаута (положительное число).
# При несоответствии — raise ValueError с понятным сообщением. Вызов в try/except. Проверить минимум на трёх наборах:
# корректные значения, отрицательный таймаут, слишком большое количество повторов.
# Решение:
def run_test_with_retries(retries, timeout):
    if not 0 <= retries <= 5:
        raise ValueError(f"Количество повторов должно быть от 0 до 5, получено: {retries}")
    if timeout <= 0:
        raise ValueError(f"Таймаут должен быть положительным, получено: {timeout}")
    print(f"Запуск теста: повторов={retries}, таймаут={timeout}")

# Корректные значения
try:
    run_test_with_retries(3, 10)
except ValueError as e:
    # Выводим результат:
    print(f"Ошибка: {e}")

# Отрицательный таймаут
try:
    run_test_with_retries(2, -5)
except ValueError as e:
    # Выводим результат:
    print(f"Ошибка: {e}")

# Слишком много повторов
try:
    run_test_with_retries(10, 5)
except ValueError as e:
    # Выводим результат:
    print(f"Ошибка: {e}")

# Пояснение:
# Проверяем диапазон через 0 <= retries <= 5.
# Таймаут — через timeout <= 0.
# raise ValueError прерывает функцию, ошибка ловится в try/except.


# Задача 4
# Условие: Создать исключение InvalidTestStatusError, наследуемое от Exception. Функция принимает статус
# теста и проверяет его (допустимы только PASS, FAIL, SKIP). При неверном — raise InvalidTestStatusError
# с сообщением. Обработать в try/except. Проверить с корректными и некорректными статусами.
# Решение:
class InvalidTestStatusError(Exception):
    pass

def validate_status(status):
    valid = ["PASS", "FAIL", "SKIP"]
    if status not in valid:
        raise InvalidTestStatusError(f"Недопустимый статус: {status}")
    print(f"Статус принят: {status}")

# Корректные статусы
for status in ["PASS", "FAIL", "SKIP"]:
    try:
        validate_status(status)
    except InvalidTestStatusError as e:
        # Выводим результат:
        print(f"Ошибка: {e}")

# Некорректный статус
try:
    validate_status("WRONG")
except InvalidTestStatusError as e:
    # Выводим результат:
    print(f"Ошибка: {e}")

# Пояснение:
# Класс InvalidTestStatusError наследуется от Exception.
# raise InvalidTestStatusError(...) — выбрасывает наше исключение.
# except InvalidTestStatusError as e — ловит именно наше исключение.


# Задача 5
# Условие: Программа получает данные из JSON-файла (название, статус, время выполнения). Определить общее
# количество, количество по статусам, список упавших, самый длительный тест, суммарное время. Использовать
# минимум один генератор списка, lambda, filter(), reduce(). Работу с файлом защитить через try/except.
# Итоговый отчёт сохранить в отдельный JSON.
# Решение:
import json
from functools import reduce


def build_report(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError as e:
        print(f"Файл не найден: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Некорректный JSON: {e}")
        return None

    try:
        tests = data["tests"]
    except KeyError as e:
        print(f"Отсутствует поле 'tests': {e}")
        return None

    try:
        total = len(tests)

        # Генератор списка
        passed_names = [t["name"] for t in tests if t["status"] == "PASS"]

        # filter + lambda
        failed_tests = list(filter(lambda t: t["status"] == "FAIL", tests))
        failed_names = [t["name"] for t in failed_tests]

        # reduce
        total_duration = reduce(lambda acc, t: acc + t["duration"], tests, 0)

        # Самый длительный тест
        longest = max(tests, key=lambda t: t["duration"])

        # Подсчёт по статусам
        statuses = ["PASS", "FAIL", "SKIP"]
        status_counts = {
            s: len([t for t in tests if t["status"] == s]) for s in statuses
        }

        report = {
            "total": total,
            "status_counts": status_counts,
            "failed_tests": failed_names,
            "passed_tests": passed_names,
            "longest_test": {"name": longest["name"], "duration": longest["duration"]},
            "total_duration": total_duration,
        }

        return report

    except KeyError as e:
        print(f"Неправильная структура данных: {e}")
        return None


def save_report(report, output_path):
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=4, ensure_ascii=False)
        # Выводим результат:
        print(f"Отчёт сохранён в {output_path}")
    except Exception as e:
        print(f"Ошибка сохранения: {e}")


report = build_report("test_results.json")
if report:
    # Выводим результат:
    print(json.dumps(report, indent=4, ensure_ascii=False))
    save_report(report, "report.json")

# Пояснение:
# try/except покрывает работу с файлом и структуру данных.
# Генератор списка — для passed_names.
# filter() + lambda — для упавших тестов.
# reduce() — для суммарного времени.
# max(..., key=lambda) — для самого длительного теста.
# Итог сохраняется в report.json
