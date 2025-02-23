def function_with_uncommon_error(x, y):
    if x == 0:
        return "Division by zero is not allowed" # Handle the error gracefully
    return x + y

result = function_with_uncommon_error(0, 5)
print(result) # Output: Division by zero is not allowed

result = function_with_uncommon_error(5, 2)
print(result)  # Output: 7