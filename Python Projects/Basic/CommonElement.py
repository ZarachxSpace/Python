def common_elements(list_a, list_b):
    sorted_list = []
    for i in list_a:
        for j in list_b:
            if i == j:
                if i not in sorted_list: 
                    sorted_list.append(i)
            else:
                continue

    return print(sorted(sorted_list))


# def common_elements(list_a, list_b):
#     set_a, set_b = set(list_a), set(list_b)
#     return sorted(set_a.intersection(set_b))

common_elements([1, 2, 2, 3, 4], [2, 3, 3, 5])
# print(common_elements([1, 2, 2, 3, 4], [2, 3, 3, 5]))
