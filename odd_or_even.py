lst = [2,4,5,36,3]

odd=0
even=0
ev=[]
od=[]
for i in lst:
    if i%2 ==0:
        ev.append(i)
        even=even+1
    else:
        od.append(i)
        print("odd-->",i)
        odd=odd+1
        
print("TOTAL of EVEN IS",even)
print("TOTAL of ODD IS",odd)

print("List of even numbers" ,ev)
print("List of odd numbers" ,od)
        
# =======================================================

lst = [2,4,5,36,3]

odd=0
even=0
for i in lst:
    if i%2 ==0:
        print("even --> " ,i)
        even=even+1
    else:
        print("odd-->",i)
        odd=odd+1
        
print("TOTAL of EVEN IS",even)
print("TOTAL of ODD IS",odd)
        
# =======================================================



