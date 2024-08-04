
def count_vowels_unoptimized(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

result = count_vowels_unoptimized("This is a simple test.")
print(result)
