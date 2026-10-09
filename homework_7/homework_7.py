# Задача 1
# Условие: Создать класс CreditCard с номером счёта и начальным балансом. Реализовать методы: deposit(amount) —
# пополнение; withdraw(amount) — снятие; show_info() — вывод номера счёта и баланса. Создать три объекта с разными
# счетами. Пополнить первую и вторую, снять с третьей. Вывести информацию о всех.
# Решение:
class CreditCard:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть > 0")
        self.balance += amount
        print(f"Счёт {self.account_number}: пополнение на {amount}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть > 0")
        if amount > self.balance:
            raise ValueError("Недостаточно средств")
        self.balance -= amount
        print(f"Счёт {self.account_number}: снятие {amount}")

    def show_info(self):
        # Выводим результат:
        print(f"Счёт: {self.account_number}, Баланс: {self.balance}")


card_1 = CreditCard("ACC001", 1000)
card_2 = CreditCard("ACC002", 500)
card_3 = CreditCard("ACC003", 2000)

card_1.deposit(500)
card_2.deposit(300)
card_3.withdraw(1000)

card_1.show_info()
card_2.show_info()
card_3.show_info()


# Задача 2
# Условие: Класс ATM хранит количество купюр номиналом 20, 50, 100. Начальное количество передаётся в __init__.
# Методы: add_money() — добавить купюры; withdraw(amount) — снять сумму. Если можно выдать — уменьшить количество
# купюр, вывести, сколько купюр каждого номинала выдано, вернуть True. Иначе вернуть False и ничего не менять.
# Решение:
class ATM:
    def __init__(self, count_20, count_50, count_100):
        self.count_20 = count_20
        self.count_50 = count_50
        self.count_100 = count_100

    def add_money(self, count_20=0, count_50=0, count_100=0):
        self.count_20 += count_20
        self.count_50 += count_50
        self.count_100 += count_100

    def withdraw(self, amount):
        # пробуем выдать купюрами 100, затем 50, затем 20
        remaining = amount
        use_100 = min(remaining // 100, self.count_100)
        remaining -= use_100 * 100

        use_50 = min(remaining // 50, self.count_50)
        remaining -= use_50 * 50

        use_20 = min(remaining // 20, self.count_20)
        remaining -= use_20 * 20

        if remaining != 0:
            print("Невозможно выдать указанную сумму")
            return False

        self.count_100 -= use_100
        self.count_50 -= use_50
        self.count_20 -= use_20

        # Выводим результат:
        print(f"Выдано: 100×{use_100}, 50×{use_50}, 20×{use_20}")
        return True


atm = ATM(10, 10, 10)
atm.add_money(count_100=5)

# Выводим результат:
atm.withdraw(380)   # 100×3, 50×1, 20×1
atm.withdraw(75)    # 50×1, 20×1
atm.withdraw(30)    # 20×1
atm.withdraw(45)    # невозможно


# Задача 3
# Условие: Базовый класс Doctor с методом treat(). Дочерние: Surgeon, Dentist, Therapist — переопределяют treat().
# Класс Patient с атрибутами treatment_plan (код) и doctor. В Therapist реализовать метод назначения врача:
# код 1 → хирург; код 2 → дантист; иначе → терапевт. После назначения сохранить врача в patient.doctor и вызвать treat().
# Решение:
class Doctor:
    def treat(self):
        print("Врач проводит общее лечение")


class Surgeon(Doctor):
    def treat(self):
        print("Хирург проводит операцию")


class Dentist(Doctor):
    def treat(self):
        print("Дантист лечит зубы")


class Therapist(Doctor):
    def treat(self):
        print("Терапевт проводит общий осмотр")

    def assign_doctor(self, patient):
        if patient.treatment_plan == 1:
            patient.doctor = Surgeon()
        elif patient.treatment_plan == 2:
            patient.doctor = Dentist()
        else:
            patient.doctor = Therapist()
        patient.doctor.treat()


class Patient:
    def __init__(self, treatment_plan):
        self.treatment_plan = treatment_plan
        self.doctor = None


# Выводим результат:
patient_1 = Patient(1)
Therapist().assign_doctor(patient_1)  # Хирург проводит операцию

patient_2 = Patient(2)
Therapist().assign_doctor(patient_2)  # Дантист лечит зубы

patient_3 = Patient(3)
Therapist().assign_doctor(patient_3)  # Терапевт проводит общий осмотр
