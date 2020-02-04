# ZADANIE 3.
# NALEŻY WYGENEROWAĆ LISTĘ LICZB OD 2 DO 5.5 ZE SKOKIEM CO 0.5,
# DANE WYNIKOWE MUSZĄ BYĆ TYPU DECIMAL.
from decimal import Decimal


def task_3(start, stop, step):
    decimal_list = []
    while True:
        if start <= stop:
            decimal_list.append(Decimal(start))
            start += step
        else:
            return decimal_list


print(task_3(2, 6.5, 0.5))