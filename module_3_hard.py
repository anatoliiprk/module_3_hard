print('')
print('Задание "Раз, два, три, четыре, пять .... Это не всё?"')
print('')

def calculate_structure_sum (*args):
    total_sum = 0
    first_element = args[0]
    if isinstance(first_element, int):
        total_sum += first_element
    elif isinstance(first_element, str):
        total_sum += len(first_element)
    elif isinstance(first_element, list) or isinstance(first_element, tuple):
        for i in range(len(first_element)):
            total_sum += calculate_structure_sum(first_element[i])
    elif isinstance(first_element, dict):
        for key, values in first_element.items():
            total_sum += len(key) + values
    elif isinstance(first_element, set):
        for j in first_element:
            total_sum += calculate_structure_sum(j)
    return total_sum

data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((),[{(2, 'Urban', ('Urban2', 35))}])]
result = calculate_structure_sum(data_structure)
print('Результат:', result)
