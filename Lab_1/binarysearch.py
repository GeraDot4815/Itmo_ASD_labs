def bs(arr, x):
    l = 0
    h = len(arr) - 1
    i = 0
    while l <= h:
        i+=1
        m = int((l + h) / 2)
        if x == arr[m]:
            return m, i
        elif x > arr[m]:
            l = m + 1
        else:
            h = m - 1

    return -1,i


arr = [2, 55, 100, 106, 112, 250, 500]
print("Your list is", arr)
num=int(input("input num from list: "))
i = bs(arr, num)

if (i == -1):
    print("Not Found...")
else:
    print("It need", i[1], "steps")