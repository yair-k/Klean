
def selection_sort_unoptimized(lst):
    for i in range(len(lst)):
        min_idx = i
        for j in range(i + 1, len(lst)):
            if lst[min_idx] > lst[j]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

result = selection_sort_unoptimized([64, 25, 12, 22, 11])
print(result)
