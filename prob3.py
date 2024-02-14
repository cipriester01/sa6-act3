def find_max(numbers, compare_func):
    if not numbers:
        return None  
    max_num = num_list[0]
    for num in num_list[1:]:
        max_num = compare_func(max_num, num)
    return max_num

num_list = [12, 45, 23, 67, 89, 34]
compare_lambda = lambda x, y: x if x > y else y
max_number = find_max(num_list, compare_lambda)
print(f"Max number: {max_number}")

