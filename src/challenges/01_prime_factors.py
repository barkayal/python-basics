def get_prime_factors(num):
    factors = []
    divisor = 2
    while divisor <= num:
        if num % divisor == 0:
            factors.append(divisor)
            num = num // divisor
        else:
            divisor += 1
    return factors

tests = [13, 630]

[print(f"{test}: {get_prime_factors(test)}") for test in tests]
