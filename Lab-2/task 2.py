x =[23,56,89,52,14,57,29,76,92]

print("input x :",x)


n = len(x)

for i in range(n):
    for j in range(n-i-1):
        if x[j] > x[j+1]:
            temp = x[j]
            x[j] = x[j+1]
            x[j+1] = temp

print("sorted x :",x)