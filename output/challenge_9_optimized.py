
def selection_sort_optimized(lst):
    for i in range(len(lst)):
        min_idx = min(range(i, len(lst)), key=lst.__getitem__)
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

print(selection_sort_optimized([64, 25, 12, 22, 11]))
