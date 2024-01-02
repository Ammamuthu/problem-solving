# Solving method 1
lst =[2,5,2,6,1]

usr=int(input("Enter the Element : "))

if usr in lst:
        print("Found")
else:
        print("no")
    
# Solving method 2
flog=0
lst =[2,5,2,6,1]
usr=int(input("Enter the Element : "))
for i in lst:
    if usr==i:
        print("Gotchaaaa")
        flog=1
        break
if flog == 0:
    print("Not here Bro ................")
        

