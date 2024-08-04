
def string_reverse_unoptimized(s):
    reversed_string = ""
    for i in range(len(s) - 1, -1, -1):
        reversed_string += s[i]
    return reversed_string

result = string_reverse_unoptimized("Hello, World!")
print(result)
