l=[]
for i in range(2,8):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        l.append(i)
print(sum(l))
print(l)