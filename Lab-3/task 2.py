import random
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

arr=[]
for i in range(5):
    arr.append(random.randint(-100, 100))
print(arr)
mysorted=bucket_sort(arr)
print(mysorted)
if mysorted==sorted(arr): print("True")
else: print("False")