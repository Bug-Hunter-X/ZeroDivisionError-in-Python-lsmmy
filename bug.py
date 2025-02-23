def function_with_uncommon_error(x, y):
    if x == 0:
        return y / x  # ZeroDivisionError will occur if x is 0
    return x + y

result = function_with_uncommon_error(0, 5)