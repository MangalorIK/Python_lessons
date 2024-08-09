data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

sum_ = 0


def calculate_structure_sum(data):
    global sum_
    # print(f"type = {type(data)}, {data}")
    # if list/tuple/set
    if isinstance(data, (list, tuple, set)):
        for value in data:
            calculate_structure_sum(value)
    # if dict
    if isinstance(data, dict):
        for key, value in data.items():
            calculate_structure_sum(key)
            calculate_structure_sum(value)
    # if number
    if isinstance(data, (int, float)):
        sum_ += data
    # if string
    elif isinstance(data, str):
        sum_ += len(data)

    return sum_


result = calculate_structure_sum(data_structure)
print(f"result is {result}")
