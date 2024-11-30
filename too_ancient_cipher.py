def generate_password(n):
    result = ""

    for x in range(1, 10):
        for y in range(x + 1, 10):
            if n % (x + y) == 0:
                result += str(x) + str(y)

    return result

n = int(input("Введите число от 3 до 20: "))
print(generate_password(n))
