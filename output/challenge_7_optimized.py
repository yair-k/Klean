
def gcd_optimized(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd_optimized(48, 18))
