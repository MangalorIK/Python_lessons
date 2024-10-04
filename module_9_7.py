def is_prime(func):
    def wrapper(first, second, third):
        result = func(first, second, third)

        d = 2
        while result % d != 0:
            d += 1

        return (f"Простое" if result == d else "Составное") + f"\n{result}"
    return wrapper


@is_prime
def sum_three(first, second, third):
    return first+second+third


result = sum_three(2, 3, 6)
print(result)