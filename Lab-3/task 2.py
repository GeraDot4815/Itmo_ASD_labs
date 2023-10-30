import random

#Блочная сортировка
def floor_up(i):
    return int(i//1)
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr
def bucket_sort(arr):
    bckts=[[] for i in range (len(arr))]
    minval=arr[0]
    maxval=arr[0]
    for i in arr:
        if i<minval: minval=i
        if i>maxval: maxval=i

    numrange=maxval-minval

    for i in arr:
        bcktidx=floor_up((i-minval) / numrange * (len(bckts)-1))
        bckts[bcktidx].append(i)

    for i in range(len(bckts)):
        bckts[i]=bubble_sort(bckts[i])


    res=[]
    for i in range(len(arr)):
        for j in range(len(bckts[i])):
            res.append(bckts[i][j])
    return res

#Пирамидальная сортировка
def swap(arr, i, j):
    res=arr
    res[i], res[j] = res[j], res[i]
    return res

def sift_down(arr, i, upper):
    res=arr
    while True:
        l, r = i*2+1, i*2+2

        if max(l, r)<upper: #this indexes is exist in now arr
            if res[i]>=max(res[l], res[r]): break #branch in tree is sorted
            elif res[l]>res[r]:
                res=swap(res, i, l)
                i = l
            else:
                res = swap(res, i, r)
                i = r

        elif l<upper: #only left element exist
            if res[l]>res[i]:
                res=swap(res, i, l)
                i = l
            else:
                break

        elif r<upper: # only right element exist
            if res[l] > res[i]:
                res = swap(res, i, l)
                i = l
            else:
                break

        else: break #no children elements in this tree
    return res
def heap_sort(arr):
    res=arr
    for i in range((len(res)-2)//2, -1, -1):
        res=sift_down(res, i, len(res))

    for end in range(len(res)-1, 0, -1):
        res=swap(res, 0, end)
        res=sift_down(res, 0, end)


    return res

#Сортировка слиянием
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

#Проверка
arr = [random.randint(-100, 100) for _ in range(7)]
print(arr)

mysorted = heap_sort(arr) #choose your sort mode

print(mysorted)
if mysorted==sorted(arr): print("True")
else: print("False")