def knapsack_max_value(N, M, K, weights, values):
    dp = [0] * (M + 1)

    for i in range(N):
        for j in range(M, K - 1, -1):
            dp[j] = max(dp[j], dp[j - K] + values[i])

    return dp[M]

N = 5  # количество экспонатов عدد المعروضات
M = 10  # количество заходов عدد الزيارات
K = 3  # вес, который может унести вор за один заход الوزن الذي يمكن أن يحمله اللص دفعة واحدة
weights = [3, 4, 1, 2, 5, ]  # веса экспонатов وزن المعروضات
values = [25, 20, 15, 30, 50 , ]  # цены экспонатов سعر المعروضات

max_stolen_value = knapsack_max_value(N, M, K, weights, values)
print("Максимальная сумма украденных ценностей:", max_stolen_value) #الحد الأقصى لحجم الأصول المسروقة

#Этот код решает задачу о рюкзаке с ограничением на количество заходов и на количество унесенного веса за один заход.