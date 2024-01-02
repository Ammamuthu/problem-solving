cont=[10,33,11,2,26,65]
cnt =len(cont)

for i in range(0,cnt):
    for j in range(i+1 ,cnt):
         if cont[i]<=cont[j]:
            temp =cont[i]
            cont[i]=cont[j]
            cont[j]=temp
print(cont)
