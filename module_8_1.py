from decimal import Decimal


def add_everything_up(a, b):
    try:
        return Decimal(str(a)) + Decimal(str(b))
    # Decimal использовался для обрезания результата 130.45600000000002 -> 130.456
    except:
        return str(a) + str(b)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
