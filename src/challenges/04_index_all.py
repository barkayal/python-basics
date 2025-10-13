def index_all(my_list, items):
    index_list = []
    for index, value in enumerate(my_list):
        if value == items:
            index_list.append([index])
        elif isinstance(my_list[index], list):
            for i in index_all(my_list[index], items):
                index_list.append([index] + i)
    return index_list

my_list = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
tests = [2, [1, 2, 3]]
[print(f"{test} => {index_all(my_list, test)}") for test in tests]