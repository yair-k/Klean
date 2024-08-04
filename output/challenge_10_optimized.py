
def count_vowels_optimized(s):
    return sum(1 for char in s if char in 'aeiouAEIOU')

print(count_vowels_optimized("This is a simple test."))
