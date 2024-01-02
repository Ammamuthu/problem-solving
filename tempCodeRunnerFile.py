lst = [2,4,5,36,3]

odd=0
even=0
ev=[]
for i in lst:
    if i%2 ==0:
        ev=[]+ev
        even=even+1
    else:
        od=[i]
        print("odd-->",i)
        odd=odd+1
        
print("TOTAL of EVEN IS",even)
print("TOTAL of ODD IS",odd)

print("List of even numbers" ,ev)
print("List of odd numbers" ,od)