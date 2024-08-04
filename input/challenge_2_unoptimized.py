
def factorial_unoptimized(n):
    if n == 0:
        return 1
    else:
        return n * factorial_unoptimized(n - 1)

result = factorial_unoptimized(10)
print(result)
