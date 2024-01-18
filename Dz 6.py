result = []
def divider(a, b):
    try:
        if a < b:
            raise ValueError
        if b > 100:
            raise IndexError
        if b == 0:
            raise ZeroDivisionError("division by zero is not allowed")
        return a/b
        if a != int:
            raise TypeError("a not number")

    except (ValueError, ZeroDivisionError, IndexError) as e :
        print(f"Exception: {type(e).__name__} - {e}")
        return None
try:
    data = {10: 2, 2: 5, "123": 4, 18: 0,  8 : 4}
    for key in data:
     res = divider(key, data[key])
     result.append(res)
except Exception as e:
    print(f"Exception: {type(e).__name__} - {e}")

print(result)