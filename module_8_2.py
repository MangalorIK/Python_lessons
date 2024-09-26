def personal_sum(numbers):
    summ = 0
    incorrect_data = 0
    for number in numbers:
        try:
            summ += number
        except TypeError:
            print('Некорректный тип данных для подсчёта суммы - ', number)
            incorrect_data += 1
    return summ, incorrect_data


def calculate_average(numbers):
    avg = 0
    is_numbers = 0
    try:
        data = personal_sum(numbers)
        for number in numbers:
            if type(number) is int or type(number) is float:
                is_numbers += 1
        avg = data[0] / is_numbers
        return avg
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
