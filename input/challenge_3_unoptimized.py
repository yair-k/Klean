
def sum_unoptimized(lst):
    total = 0
    for i in range(len(lst)):
        total += lst[i]
    return total

result = sum_unoptimized([1, 2, 3, 4, 5])
print(result)
