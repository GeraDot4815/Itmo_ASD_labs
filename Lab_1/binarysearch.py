import random


def bs(arr, x):
    l = 0
    h = len(arr) - 1
    i = 0
    while l <= h:
        i += 1
        m = int((l + h) / 2)
        # check if x is present at mid
        if x == arr[m]:
            return m, i
        # if x is greater ignore left half
        elif x > arr[m]:
            l = m + 1
        # if x is samaller ignore right half
        else:
            h = m - 1

    return -1, i


arr = [2, 55, 100, 106, 112, 250, 500]
print("Your list is", arr)
num = int(input("input num from list to search for: "))
i = bs(arr, num)


# arr2 = []
# for j in range(6):
#     arr2.append(int(input(f"array[{j}] = ")))
# print("Your list is", arr2)
# num = int(input("input num from list to search for: "))
# arr2 = sorted(arr2)
# i = bs(arr2, num)

# arr3 = []
# for j in range(15):
#     arr3.append(random.randint(0, 500))
# arr3 = sorted(arr3)
# print("Your list is", arr3)
# num = int(input("input num from list to search for: "))
# i = bs(arr3, num)

if (i[0] == -1):
    print("Not Found... It needs", i[1], "steps")
else:
    print("Index =", i[0], ", it needs", i[1], "steps")
