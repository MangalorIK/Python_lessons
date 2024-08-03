def get_password(num):
    password = ""
    for j in range(1, num // 2 + 1):
        for k in range(1, 21):
            if j == k or j > k:
                continue
            if num % (j + k) == 0:
                password += f"{j}{k}"
    return password


number = 0
while number < 3 or number > 20:
    number = int(input("Введите число от 3 до 20: "))

print(get_password(number))
