from data import DATA, DATE, NAME, PREP
from datetime import date
def __binary_search(arr, low, high, x, key):
    """Binary Search Core"""
    if high >= low:
        mid = (high + low) // 2

        arr_mid = arr[mid] if key is None else key(arr[mid])
        if arr_mid == x:
            return mid
        elif arr_mid > x:
            return __binary_search(arr, low, mid - 1, x, key=key)
        else:
            return __binary_search(arr, mid + 1, high, x, key=key)
    else:
        return -1

def binary_search(arr, x, key=None):
    """Binary Search Algorithn"""
    return __binary_search(arr, 0, len(arr) - 1, x, key=key)
# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Get Date
dt = date.fromisoformat(input("Введите дату: "))
# Searching
dt = binary_search(sorted(DATA, key=lambda i: i[DATE]), dt, key=lambda i: i[DATE])


# Printing output result
if dt == -1:
    print("В этот день ученые отдыхали")
else:
    dt = DATA[dt]
    print(f'{dt[NAME]} создал препарат: {dt[PREP]} - {dt[DATE].strftime("%d.%m.%Y")}')