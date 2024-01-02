
a=1
b=2

temp=a
a=b
b=temp
print(a)
print(b)

# Swapping first element and Last Element in a List
def swap(list):
    siz = len(list)

    temp = list[0]
    list[0]=list[siz-1]
    list[siz-1] = temp
    return(list)
    
list= [1,2,3,4]
# print(list)
print(swap(list))

# 3 variables swapping

a=10  #30 10 20
b=20
c=30
temp=a
a=c
c=b
b=temp

print(a,b,c)


