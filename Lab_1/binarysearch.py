def bs(arr, x):
    l = 0
    h = len(arr) - 1
    i = 0
    while l <= h:
        i += 1
        m = int((l + h) / 2)
        #check if x is present at maid
        if x == arr[m]: 
            return m, i
        #if x is greater. ignore left half
        elif x > arr[m]:
            l = m + 1
         #if x is smaller, ignore right half
        else:
            h = m - 1

    return -1, i


arr5 = [2, 55, 100, 106, 112, 250, 500]
print("Your list is", arr5)
num = int(input("input num from list: "))
i = bs(arr5, num)


if (i[0] == -1):
    print("Not Found... It needs", i[1], "steps")
else:
    print("index = ", i[0], "It needs", i[1], "steps")
