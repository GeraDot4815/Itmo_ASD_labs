def find_exit(maze):
    n = len(maze)
    visited = [[False] * n for _ in range(n)]

    def dfs(row, col):
        #Проверяем границы массива
        if row < 0 or row >= n or col < 0 or col >= n:
            return False
        #Если зашли в стену или вернулись к пройденной точке, выхода нет
        if maze[row][col] == 1 or visited[row][col]:
            return False

        visited[row][col] = True #Отмечаем данную точку

        if row == 0 or row == n - 1 or col == 0 or col == n - 1: #Если мы у выхода, то выход найден
            return True

        if dfs(row - 1, col):  # Вверх
            return True

        if dfs(row + 1, col):  # Вниз
            return True

        if dfs(row, col - 1):  # Влево
            return True

        if dfs(row, col + 1):  # Вправо
            return True

        return False

    # Начинаем поиск выхода с первой строки
    for col in range(n):
        if maze[0][col] == 0:
            if dfs(0, col):
                return True

    return False


# Пример использования
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
]

if find_exit(maze):
    print("Выход найден")
else:
    print("Выход не найден")