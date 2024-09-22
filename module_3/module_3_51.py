

def get_multiplied_digits(number):
    str_number = str(number)

    result = 1
    zeroes_flag = True

    for digit in str_number:
        digit = int(digit)
        if digit != 0:
            result *= digit
            zeroes_flag = False

    return result

result = get_multiplied_digits(40230)
print(result)
