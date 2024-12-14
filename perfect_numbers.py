def classify(number):
    """
    Determine if a number is perfect, abundant, 
    or deficient based on Nicomachus' (60 - 120 CE) 
    classification scheme for positive integers
    from exercism.org's python path.
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    factors = [i for i in range(1, number) if (number % i == 0 and i <= (number / 2))]
    if sum(factors) == number:
        result = 'perfect'
    elif sum(factors) > number:
        result = 'abundant'
    else:
        result = 'deficient'
    return result

print(classify(28))
