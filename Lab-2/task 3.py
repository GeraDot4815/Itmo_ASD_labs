# 1. Алгоритм со сложностью O(3n):

def sum_arrays(arr1, arr2, arr3):
    n = len(arr1)
    summ = 0

    for i in range(n):

        summ += arr1[i] + arr2[i] + arr3[i]

    return summ

# Алгоритм суммирует элементы трех массивов длиной n.

# 2. Алгоритм со сложностью O(nlogn):


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
# find the middle index(العثور على الفهرس الأوسط)
    mid = len(arr) // 2  # integer
    left = merge_sort(arr[:mid])  # left part
    right = merge_sort(arr[mid:])  # right part
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

# Алгоритм сортирует массив длиной n с использованием алгоритма слияния (merge sort).

# 3. Алгоритм со сложностью O(n!):


def permutations(arr):
    result = []

    def permute(current, remaining):
        if len(remaining) == 0:
            result.append(current)
        else:
            for i in range(len(remaining)):
                next_perm = current + [remaining[i]]
                remaining_copy = remaining[:i] + remaining[i+1:]
                permute(next_perm, remaining_copy)

    permute([], arr)
    return result


# print(permutations([8, 5, 99, 10, 88]))


# Алгоритм генерирует все перестановки массива длиной n.

# 4. Алгоритм со сложностью O(n^3):


def matrix_multiplication(matrix1, matrix2):
    n = len(matrix1)
    result = [[0] * n for _ in range(n)]
    print(result)

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result


a = [[7, 8, 9], [10, 11, 12]]
b = [[1, 2], [3, 4], [5, 6]]

# print(matrix_multiplication(a, b))
# Алгоритм умножает две матрицы размером nxn.

# 5. Алгоритм со сложностью O(3log(n)):


# def search_values(arr, value1, value2, value3):

#     index1 = index2 = index3 = -1
#     indxs = [index1, index2, index3]
#     values = [value1, value2, value3]
#     for i in range(3):
#         left = 0
#         right = len(arr) - 1
#         while left <= right:
#             middle = (left + right) // 2

#             if arr[middle] == values[i]:
#                 indxs[i] = middle

#             if arr[middle] < values[i]:
#                 left = middle + 1
#             else:
#                 right = middle - 1

#     return [index1, index2, index3]


# print(search_values([1, 2, 4, 67, 8], 2, 67, 4))


def bs(arr, x):
    l = 0
    h = len(arr) - 1
    while l <= h:
        m = int((l + h) / 2)
        # check if x is present at mid
        if x == arr[m]:
            return m
        # if x is greater ignore left half
        elif x > arr[m]:
            l = m + 1
        # if x is samaller ignore right half
        else:
            h = m - 1

    return -1


values = [2, 67, 4]
arr = [1, 2, 4, 67, 8]

for i in range(len(values)):
    print(bs(arr, values[i]))
# Алгоритм осуществляет бинарный поиск трех значений в отсортированном массиве длиной n.
