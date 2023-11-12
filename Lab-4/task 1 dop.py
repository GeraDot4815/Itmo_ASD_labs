#()
lR=[]
rR=[]
#[]
lSq=[]
rSq=[]
#{}
lF=[]
rF=[]
s=input("Enter string: ")

flag=True

for i in range(len(s)):
    if s[i]=="(": lR.append(i)
    elif s[i]==")": rR.append(i)


    if s[i]=="[": lSq.append(i)
    elif s[i]=="]": rSq.append(i)


    if s[i]=="{": lF.append(i)
    elif s[i]=="}": rF.append(i)

    if len(rR)>len(lR):
        print(rR[-1])
        flag=False
        break

    if len(rSq)>len(lSq):
        print(rSq[-1])
        flag=False
        break

    if len(rF)>len(lF):
        print(rF[-1])
        flag=False
        break
if len(lR)>len(rR):
    print(lR[0])
    flag=False

if len(lSq)>len(rSq):
    print(lSq[0])
    flag=False

if len(lF)>len(rF):
    print(lF[0])
    flag=False

if flag: print("Все отлично!")