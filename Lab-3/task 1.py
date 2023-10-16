import random
import timeit


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def comb_sort(arr):
    gap = len(arr)
    shrink = 1.3
    sorted = False

    while not sorted:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted = True
        i = 0
        while i + gap < len(arr):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted = False
            i += 1

    return arr


# Генерируем случайный массив для сортировки
arr = [random.randint(0, 1000) for _ in range(10000)]

# Замеряем время выполнения функции быстрой сортировки
quick_sort_time = timeit.timeit(lambda: quick_sort(arr), number=1)

# Замеряем время выполнения функции сортировки расческой
comb_sort_time = timeit.timeit(lambda: comb_sort(arr.copy()), number=1)

print(f'Время выполнения функции быстрой сортировки: {quick_sort_time} сек.')
print(f'Время выполнения функции сортировки расческой: {comb_sort_time} сек.')