def bs(arr, x):
    l = 0
    h = len(arr) - 1
    i = 0
    while l <= h:
        i+=1
        m = int((l + h) / 2)
        #check if x is present at mid 
        if x == arr[m]:
            return m, i
        #if x is greater ignore left half
        elif x > arr[m]:
            l = m + 1
        #if x is samaller ignore right half
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