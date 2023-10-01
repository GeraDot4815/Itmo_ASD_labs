x=int(input("Введите количество городов: "))
roads=[0]*x
allcity=set()
for i in range(x):
    roads[i]=[0]*x

for i in range(x):
    for j in range(i,x):
        if i==j: roads[i][j]=1
        else:
            value=int(input(f"Дорога между городами {i} и {j}: "))
            roads[i][j]=value
            roads[j][i]=value

for i in range(x):
    cityes=[i]
    for j in range(x):
        if i!=j:
            if roads[i][j]==1:
                cityes.append(j)
    allcity.add(tuple(cityes))

for i in range(x):
    print(roads[i])
print(allcity)
def compare(allcity):
    for city1 in allcity:
        for city2 in allcity:

            if city1!=city2:
                c1 = (list(city1))
                #c1.pop(0)
                c2 = (list(city2))
                #c2.pop(0)
                inters=set(c1).intersection(set(c2))
                if inters!=set():
                    allcity.remove(city1)
                    allcity.remove(city2)
                    allcity.add(tuple(c1)+tuple(c2))
                    print(allcity)
                    return allcity
    return {1}
while compare(allcity)!= {1}:
    allcity =compare(allcity)
print(len(allcity))