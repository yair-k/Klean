
def gcd_unoptimized(a, b):
    while b != 0:
        temp = a
        a = b
        b = temp % b
    return a

result = gcd_unoptimized(48, 18)
print(result)
