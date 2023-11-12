import random

N0=[]
#N0=[0, 1, 2, 3, 2, 3, 4, 5, 6, 7, 8, 9] #4 and 8
if N0==[]:
    n=int(input("input n: "))
    N=[random.randint(-100, 101) for i in range(n) ]
else: N=N0
print(N)

maxposl=[]
now=[N[0]]

for i in range(1, len(N)):
    if N[i]>now[-1]:
        now.append(N[i])
    else:
        if len(now)>len(maxposl):
            maxposl=now
        now=[N[i]]

if len(now)>len(maxposl):
    maxposl=now

print(len(maxposl), maxposl)