
"""
This module provides functions to convert numbers between different bases.
Functions:
    tobase10(input_base, digits):
    frombase10(digits, output_base):
    rebase(input_base, digits, output_base):
Example usage:
"""
#  input_base = 10
# digits = [23]
# output_base = 2
# print(f"You've got a {digits} base {input_base} to convert to base {output_base}")

def tobase10(input_base, digits):
    exponent = len(digits) - 1
    result = sum([digits[i] * input_base ** (exponent - i) for i in range(len(digits))])
    return result

def frombase10(digits, output_base):
    number = digits[0]
    result = []
    while number > 0:
        quotient = number // output_base
        remainder = number % output_base
        result.append(remainder)
        number = quotient
    return result[::-1]

def rebase(input_base, digits, output_base):
    if input_base < 2:  # Add this check at the beginning
        raise ValueError("input base must be >= 2")
    if output_base < 2:  # Add this check at the beginning
        raise ValueError("output base must be >= 2")
    for digi in digits:
        if digi < 0:
            raise ValueError("all digits must satisfy 0 <= d < input base")
        if digi >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
    result = []
    if sum(digits) == 0:
        result.append(0)
    elif input_base == 10:
        new_digits = [int("".join(map(str, digits)))]
        return frombase10(new_digits, output_base)
    elif input_base != 10 and output_base == 10:
        base10 = tobase10(input_base, digits)
        result = [int(num) for num in str(base10)]
    elif input_base != 10 and output_base != 10:
        new_digits = [tobase10(input_base, digits)]
        return frombase10(new_digits, output_base)
    return result
rebase(2, [1, 0, 1, 0, 1, 0], 10)
