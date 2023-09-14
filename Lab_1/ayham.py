def bs(arr, x):
    l = 0
    h = len(arr) - 1

    while l <= h:
        m = int((l + h) / 2)
        if x == arr[m]:
            return m
        elif x > arr[m]:
            l = m + 1
        else:
            h = m - 1

    return -1


arr = [2, 55, 100, 106, 112, 250, 500]

i = bs(arr, 100)
if (i == -1):
    print("Not Found...")
else:
    print("It is on index", i)