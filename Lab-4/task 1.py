lefts=[]
rights=[]
s=input("Enter string: ")

flag=True

for i in range(len(s)):
    if s[i]=="(": lefts.append(i)
    elif s[i]==")": rights.append(i)

    if len(rights)>len(lefts):
        print(rights[-1])
        flag=False
        break
if len(lefts)>len(rights):
    print(lefts[0])
    flag=False
if flag: print("Все отлично!")