
def max_unoptimized(lst):
    maximum = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > maximum:
            maximum = lst[i]
    return maximum

result = max_unoptimized([1, 5, 3, 9, 2])
print(result)
