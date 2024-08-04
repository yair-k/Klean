
def is_prime_unoptimized(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

result = is_prime_unoptimized(29)
print(result)
