def Matrix_Chain(p, i , j):
    if i == j:
        return 0
    k = j - 1
    count = (Matrix_Chain(p, i, k)
             + Matrix_Chain(p, k + 1, j)
             + p [i-1] * p[k] * p[j])
    return count

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    N = len(arr)

    print("Minimum number of multiplications is :",Matrix_Chain(arr, 1 , N-1))
