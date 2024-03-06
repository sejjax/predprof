from data import DATA, NAME, PREP, DATE

def quick_sort(array):
    """Функция быстрой сортировки """
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[0][DATE]
        for x in array:
            if x[DATE] < pivot:
                less.append(x)
            elif x[DATE] == pivot:
                equal.append(x)
            elif x[DATE] > pivot:
                greater.append(x)
        return quick_sort(less)+equal+quick_sort(greater)
    else: return array

new_data = quick_sort(DATA)[:5]

for i in new_data:
    print(f'{i[NAME]}: {i[PREP]}')
