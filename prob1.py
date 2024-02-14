sum_of_digits = lambda num: sum(int(digit) for digit in str(num))
num = 12345
result = sum_of_digits(num)
print(f"Sum of digits in '{num}': {result}")
