result = []

def divider(a, b):
    if a < b:
        raise ValueError("a має бути більшим або дорівнювати b")
    if b > 100:
        raise IndexError("b має бути менше або дорівнювати 100")
    if b == 0:
        raise ZeroDivisionError("Не можна ділити на нуль")
    return a / b

data = {("10", "2"): 2, ("2", "5"): 5, ("123", "4"): 4, ("18", "0"): 0, ("8", "4"): 4}

for (key_a, key_b), value in data.items():
    try:
        res = divider(float(key_a), float(key_b))
        result.append(res)
    except (ValueError, IndexError, ZeroDivisionError) as e:
        print(f"Error for keys {key_a}, {key_b}, value {value}: {e}")
        result.append(float('nan'))

print(result)
