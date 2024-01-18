result = []

def divider(a, b):
    if a < b:
        raise ValueError("a має бути більше або рівне b")
    if b > 100:
        raise IndexError("b не може бути більше 100")
    if b == 0:
        raise ZeroDivisionError("b не може бути рівним 0")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}

for key, value in data.items():
    try:
        res = divider(key, value)
        result.append(res)
    except (ValueError, IndexError, ZeroDivisionError) as e:
        print(f"Помилка при обробці ключа {key}: {e}")

print(result)