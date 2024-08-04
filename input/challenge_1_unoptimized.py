
def fibonacci_unoptimized(n):
    if n <= 1:
        return n
    else:
        return fibonacci_unoptimized(n - 1) + fibonacci_unoptimized(n - 2)

result = [fibonacci_unoptimized(i) for i in range(10)]
print(result)
